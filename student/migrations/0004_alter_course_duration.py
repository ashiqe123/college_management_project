# Generated by Django 4.1.6 on 2023-03-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.TextField(default=0, max_length=30),
        ),
    ]
