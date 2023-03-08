from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    course_name=models.CharField(max_length=255,null=True,blank=True)
    course_fee=models.IntegerField(null=True,blank=True)
    duration=models.TextField(default=0,max_length=30)

class Students(models.Model):
    s_name=models.TextField(max_length=255)
    s_address=models.TextField(max_length=255)
    s_dob=models.DateField(null=True,blank=True)
    s_phone=models.IntegerField(null=True,blank=True)
    s_education=models.CharField(max_length=255)
    j_date=models.DateField(default=0,null=True,blank=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)







class staff(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    address=models.TextField(max_length=255,null=True)
    phone=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=50 ,null=True,blank=True)
    dob=models.DateField()
    profile=models.ImageField(upload_to='profile/',null=True)
