# Generated by Django 4.1.6 on 2023-03-07 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_staff_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='profile',
        ),
        migrations.AddField(
            model_name='staff',
            name='image',
            field=models.ImageField(default=1, upload_to='image/'),
            preserve_default=False,
        ),
    ]
