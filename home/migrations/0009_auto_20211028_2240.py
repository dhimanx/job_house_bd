# Generated by Django 3.1.8 on 2021-10-28 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20211028_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='all_cv',
            name='jobs',
        ),
        migrations.AddField(
            model_name='all_cv',
            name='address',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='all_cv',
            name='cgpa',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='all_cv',
            name='skill',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='all_cv',
            name='university',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='all_cv',
            name='email',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='all_cv',
            name='name',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='all_cv',
            name='username',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
