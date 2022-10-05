# Generated by Django 4.0.4 on 2022-10-04 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_remove_studentmodules_module_instructor'),
        ('teachers', '0002_rename_email_teacherinfo_teacher_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherinfo',
            name='module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.studentmodules'),
        ),
    ]
