# Generated by Django 4.0.4 on 2022-10-10 02:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='lecturersubInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherDeptInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('teacher_email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('teacher_cellphone', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('Faculty', models.CharField(blank=True, choices=[('Education', 'Education'), ('Enginnering', 'Enginnering'), ('Law', 'Law'), ('Humanities', 'Humanities'), ('Arts', 'Arts'), ('Sciences', 'Sciences'), ('Health Science', 'Health Sciences')], max_length=100, null=True)),
                ('module', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_modules', to='students.studentmodules')),
                ('name', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]