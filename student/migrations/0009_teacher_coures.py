# Generated by Django 4.1.6 on 2023-03-06 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_remove_teacher_coures'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='coures',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.course'),
            preserve_default=False,
        ),
    ]
