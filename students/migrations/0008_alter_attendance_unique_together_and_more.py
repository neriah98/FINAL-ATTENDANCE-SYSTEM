# Generated by Django 4.0.4 on 2022-10-07 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_remove_studentmodules_module_instructor'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='studentmodules',
            name='session',
        ),
        migrations.AddField(
            model_name='attendance',
            name='session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='students.studentsession'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='time',
            field=models.TimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentsession',
            name='module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.studentmodules'),
        ),
        migrations.AddField(
            model_name='studentsession',
            name='session_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='date',
        ),
    ]