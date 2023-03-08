from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login
from .models import Course,Students,staff
from django.contrib.auth.decorators import login_required


def landpage(request):
    crs=Course.objects.all()
    
   
    return render(request,'landpage.html',{'crs':crs})

def loginpage(request):
    return render(request,'login.html')



def user_creation(request):
    if request.method=='POST':
        first_name=request.POST['first']
        last_name=request.POST['last']
        username=request.POST['user']
        mail=request.POST['mail']
        password1=request.POST['pas']
        password2=request.POST['pas1']
        dob=request.POST['dob']
        address=request.POST['address']
        phone=request.POST['phone']
        gender=request.POST['gender']
        course=request.POST['sel']
        crs=Course.objects.get(id=course)
        if request.FILES.get('profile' )  is not None:
            profile=request.FILES['profile']
        else:
            profile="/static/images/alt.jpg"


        if password2==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"User name already exists")
                return redirect('landpage')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password1,
                    email=mail,
                    )
                user.save()
                u=User.objects.get(id=user.id)
                Staff=staff(user=u,dob=dob,address=address,phone=phone,gender=gender,profile=profile,course=crs)
                messages.info(request,"added succesfully")

                Staff.save()              
                return redirect('loginpage')    
               
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('landpage')   
                


    return render(request,'landpage.html')


def do_login(request):
    if request.method=='POST':
        username=request.POST['user']
        password=request.POST['psw']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('home')
            else:
                
                login(request,user)
                auth.login(request,user)
                return redirect('stf')
    return render(request,'login.html')

@login_required(login_url='loginpage')
def home(request):
    obj=Course.objects.all().count()
    stff=staff.objects.all().count()
    std=Students.objects.all().count()
    return render(request,'home.html',{'obj':obj,'s':stff,'std':std})

@login_required(login_url='loginpage')
def user_home(request):
    return render(request,'user_home.html')

@login_required(login_url='loginpage')
def course(request):
    return render(request,'add_course.html')

@login_required(login_url='loginpage')
def add_course(request):
    if request.method=='POST':
        course_name=request.POST['course_name']
        course_fee=request.POST['course_fee']
        duration=request.POST['duration']
        if Course.objects.filter(course_name=course_name).exists():
            messages.info(request,'Course Already Exists !!!')
            return redirect('add_course')
        else:
            course=Course(course_name=course_name,course_fee=course_fee,duration=duration)
            course.save()
            messages.info(request,'Added Successefully')
            return redirect('add_course')
    return render(request,'add_course.html')

@login_required(login_url='loginpage')
def show_course(request):
    shc=Course.objects.all()
    return render(request,'show_course.html',{'shc':shc})

@login_required(login_url='loginpage')
def student(request):
    cours=Course.objects.all()
    return render(request,'add_student.html',{'cr':cours})


@login_required(login_url='loginpage')
def sh_staff(request):
    stf=staff.objects.all()
    return render(request,'showstaf.html',{'stf':stf})


@login_required(login_url='loginpage')

def add_student(request):
    if request.method=='POST':
        s_name=request.POST['sn']
        s_address=request.POST['sa']
        s_dob=request.POST['dob']
        s_phone=request.POST['sp']
        s_education=request.POST['edu']
        j_date=request.POST['jd']
        crs=request.POST['cn']
        course=Course.objects.get(id=crs)
        if s_dob=="":
            dob=0
            messages.warning(request,"Enter a Number value")
            return redirect('student')
        if j_date=="":

            j_date='1999-10-10'
        student=Students(s_name=s_name,s_address=s_address,s_dob=s_dob,s_phone=s_phone,
                         s_education=s_education,j_date=j_date,course=course)
        student.save()
        return redirect('home')
    return render(request,'add_student.html')

@login_required(login_url='loginpage')

def show_student(request):
    std=Students.objects.all()
    return render(request,'show_student.html',{'std':std})

@login_required(login_url='loginpage')

def edit(request,pk):
    edit_course=Course.objects.all()
    edit_student=Students.objects.get(id=pk)
    return render(request,'edit_student.html',{'ecrs':edit_course,'estd':edit_student})

@login_required(login_url='loginpage')

def edit_student(request,pk):
    if request.method=='POST':
        estd=Students.objects.get(id=pk)
        estd.s_name=request.POST['sname']
        estd.s_address=request.POST['sad']
        estd.s_dob=request.POST['dob']
        estd.s_phone=request.POST['sp']
        estd.j_date=request.POST['jod']
        estd.s_education=request.POST['edu']
        course=request.POST['sel']
        estd.course=Course.objects.get(id=course)
        estd.save()
        return redirect('home')
    return render(request,'edit_student.html')

@login_required(login_url='loginpage')

def Delete(request,pk):
    stud=Students.objects.get(id=pk)
    stud.delete()
    return redirect('show_student')

@login_required(login_url='loginpage')

def stf(request):
    if request.user.is_authenticated:
        user_id=request.user.id
        staf=staff.objects.get(user=user_id)
        
        return render(request,'user_home.html',{'staf':staf})

@login_required(login_url='loginpage')

def e_tcr(request):   
     if request.user.is_authenticated:
        user_id=request.user.id
        edit_course=Course.objects.all()
        edit_staf=staff.objects.get(user=user_id)
        user=User.objects.get(id=user_id)
        if request.method == 'POST':
            user.first_name=request.POST['first']
            user.last_name=request.POST['last']
            user.username=request.POST['user']
            user.email=request.POST['email']
            user.password=request.POST['pas']
            user.save()
            edit_staf.address=request.POST['address']
            edit_staf.phone=request.POST['phone']
            edit_staf.dob=request.POST['dob']
            edit_staf.address=request.POST['address']
            edit_staf.phone=request.POST['phone']
            edit_staf.gender=request.POST['gender']
            course=request.POST['sel']
            edit_staf.course=Course.objects.get(id=course)
            edit_staf.profile=request.FILES['profile']
            
                
            edit_staf.save()
            return redirect('stf')
        return render(request,'edit_teacher.html',{'stf':edit_staf,'crs':edit_course})
     
@login_required(login_url='loginpage')
def lgout(request):
    auth.logout(request)
    return render(request,'login.html')


def Dele(request,pk):
    stf=staff.objects.get(user=pk)
    stf.delete()
    return redirect('sh_staff')
