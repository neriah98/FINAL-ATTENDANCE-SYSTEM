from django.shortcuts import render, get_object_or_404, redirect ,HttpResponse
from .models import LecturerInfo
from django.contrib.auth.models import User 
from .forms import CreateLecturer
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import SignUpForm , SessionForm
from django.contrib.auth import login
from students.models import *
#For Recognizer
import cv2
import numpy as np
import face_recognition
import os
from  datetime import datetime

import pandas as pd


from datetime import date
# Create your views here.
def lecturer_list(request):
    lecturers = LecturerInfo.objects.all()

    paginator = Paginator(lecturers, 10)
    page = request.GET.get('page')
    paged_lecturers = paginator.get_page(page)
    context = {
        "lecturers": paged_lecturers
    }
    return render(request, "lecturers/lecturer_list.html", context)


def single_lecturer(request, lecturer_id):
    single_lecturer = get_object_or_404(LecturerInfo, pk=lecturer_id)
  
    context = {
        "single_lecturer": single_lecturer,
       
    }
    return render(request, "lecturers/single_lecturer.html", context)


def create_lecturer(request):
    if request.method == "POST":
        forms = CreateLecturer(request.POST, request.FILES or None)

        if forms.is_valid():
            forms.save()
        messages.success(request, "Lecturer Registration Successfully!")
        return redirect("lecturers:lecturer_list")
    else:
        forms = CreateLecturer()

    context = {
        "forms": forms
    }
    return render(request, "lecturers/create_lecturer.html", context)


def edit_lecturer(request, pk):
    lecturer_edit = LecturerInfo.objects.get(id=pk)
    edit_lecturer_forms = CreateLecturer(instance=lecturer_edit)

    if request.method == "POST":
        edit_lecturer_forms = CreateLecturer(request.POST, request.FILES or None, instance=lecturer_edit)

        if edit_lecturer_forms.is_valid():
            edit_lecturer_forms.save()
            messages.success(request, "Edit Lecturer Info Successfully!")
            return redirect("lecturers:lecturer_list")

    context = {
        "edit_lecturer_forms": edit_lecturer_forms
    }
    return render(request, "lecturers/edit_lecturer.html", context)


def delete_lecturer(request, lecturer_id):
    lecturer_delete = LecturerInfo.objects.get(id=lecturer_id)
    lecturer_delete.delete()
    messages.success(request, "Delete Lecturer Info Successfully")
    return redirect("lecturers:lecturer_list")


def register(request):
 
    if request.method != 'POST':
        # Display blank registration form. 
        form = SignUpForm()
    else:
        # Process completed form.
        form = SignUpForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            get_id = form.instance.id  # get the id of a use--it has a username inside
            users = User.objects.get(id=get_id) # get the new user
            print(users)
            lecturerProfiles = LecturerInfo.objects.create( name = users , lecturer_email=users.email,full_name=users.get_full_name())
            lecturerProfiles.save()

            new_user.save()
            return redirect("login")
            # login(request, new_user)
            # return redirect('home')
    context = {'form': form}
    return render(request, 'lecturers/registration/register.html', context)


def session(request):
    if request.method == "POST":
        form = SessionForm(request.POST)

        if form.is_valid():
            form.save()
        messages.success(request, "Session created Successfully!")
        return redirect("home")
    else:
        form = SessionForm()

    context = {'form': form}
    return render(request, "lecturers/session.html" , context  )

def single_session(request, session_id):
    session = StudentSession.objects.get(id=session_id)
    context = {"session":session}
    return render(request,"lecturers/single_session.html",context)



def recognizer_attendance(request):
    path = 'media'
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)

    for cl in myList:
         curImg = cv2.imread(f'{path}/{cl}')
         images.append(curImg)
         classNames.append(os.path.splitext(cl)[0])
         print(classNames)

    
    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList


    #  #Creating a csv file
    # response = HttpResponse(content_type='text/csv')  
    # response['Content-Disposition'] = 'attachment; filename=attendance.csv'

    # #Create a csv writer
    # writer = csv.writer(response)
    def markAttendance(name):
        with open('lecturers/Attendance.csv','r+') as f:
            # adding header
            # headerList = ['Student Number', 'Module' ,'Session Time']

            # f.to_csv('lecturers/Attendance.csv', header=headerList, index=False)
            # file2 = pd.read_csv("gfg2.csv")


            myDataList = f.readlines()
            nameList=[]

            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtString= now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString}')


    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    cap = cv2.VideoCapture(1)


    while True:
        i = 0
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurrFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurrFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            matchIndex = np.argmin(faceDis)  # this will be our best match
            i = i+1

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name + i.__str__(), (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                markAttendance(name)
            else:
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (255, 0, 0), cv2.FILLED)


            

        cv2.imshow('webcam',img)
        cv2.waitKey(0)
        #return render(request, "lecturers/recognizer_attendance.html")
        return render(request, "lecturers/attendance_success.html")
        # return HttpResponse('Attendance Marked Sucessfully')

def attendance_report(request):
    file = pd.read_csv("gfg.csv")
    print("\nOriginal file:")
    print(file)

    # adding header
    headerList = ['id', 'name', 'profession']
  
# converting data frame to csv
    file.to_csv("gfg2.csv", header=headerList, index=False)
  
# display modified csv file
    file2 = pd.read_csv("gfg2.csv")
    print('\nModified file:')
    print(file2)


   






















            













    




