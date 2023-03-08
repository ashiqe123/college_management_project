from django.urls import path
from . import views
urlpatterns = [
    path('',views.landpage,name='landpage'),
    path('user_creation',views.user_creation,name='user_creation'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('do-login',views.do_login,name='do_login'),
    path('home',views.home,name='home'),
    path('user_home',views.user_home,name='user_home'),
    path('course',views.course,name='course'),
    path('add_course',views.add_course,name='add_course'),
    path('show_course',views.show_course,name='show_course'),
    path('student',views.student,name='student'),
    path('add_student',views.add_student,name='add_student'),
    path('show_student',views.show_student,name='show_student'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('edit_student/<int:pk>',views.edit_student,name='edit_student'),
    path('Delete/<int:pk>',views.Delete,name='Delete'),
    path('stf',views.stf,name='stf'),
    path('e_tcr',views.e_tcr,name='e_tcr'),
    path('lgout',views.lgout,name='lgout'),
    path('sh_staff',views.sh_staff,name='sh_staff'),
    path('Dele/<int:pk>',views.Dele,name='Dele')
   
]