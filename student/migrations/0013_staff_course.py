# Generated by Django 4.1.6 on 2023-03-06 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_delete_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.course'),
            preserve_default=False,
        ),
    ]
