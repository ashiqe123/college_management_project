# Generated by Django 4.1.6 on 2023-03-04 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_teacher_coures'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='coures',
        ),
    ]