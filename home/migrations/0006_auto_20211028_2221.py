# Generated by Django 3.1.8 on 2021-10-28 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='address',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='cgpa',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='college',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='email',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='school',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='skill',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='university',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='username',
        ),
    ]
