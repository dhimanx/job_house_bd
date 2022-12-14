# Generated by Django 3.1.8 on 2021-10-28 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='username',
            field=models.CharField(blank=True, max_length=99, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='address',
            field=models.CharField(blank=True, max_length=99, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='cgpa',
            field=models.CharField(blank=True, max_length=99, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='college',
            field=models.CharField(blank=True, max_length=99, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='email',
            field=models.CharField(blank=True, max_length=99, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='name',
            field=models.CharField(blank=True, max_length=99, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='phone',
            field=models.CharField(blank=True, max_length=99, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='school',
            field=models.CharField(blank=True, max_length=99, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='skill',
            field=models.CharField(blank=True, max_length=99, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='university',
            field=models.CharField(blank=True, max_length=99, null=True),
        ),
    ]
