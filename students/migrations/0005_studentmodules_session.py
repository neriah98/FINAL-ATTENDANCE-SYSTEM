# Generated by Django 4.0.4 on 2022-10-04 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_studentinfo_faculty_studentinfo_student_cellphone'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodules',
            name='session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.studentsession'),
        ),
    ]