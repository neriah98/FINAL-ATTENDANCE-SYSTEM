# Generated by Django 4.0.4 on 2022-10-11 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecturers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherinfo',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]