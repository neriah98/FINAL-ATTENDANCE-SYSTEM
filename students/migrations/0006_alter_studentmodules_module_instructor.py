# Generated by Django 4.0.4 on 2022-10-04 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_rename_email_teacherinfo_teacher_email_and_more'),
        ('students', '0005_studentmodules_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodules',
            name='module_instructor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teachers.teacherinfo'),
        ),
    ]