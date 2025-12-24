from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name='Task'
urlpatterns=[
    path('Home',views.Home_view,name='Home'),
    path('Task/',views.Task_view,name='task'),
    path('',views.Login_view,name='Login'),
    path('update/<str:slug>',views.Task_update,name='task_update'),
    path('delete/<str:slug>',views.Delete_task,name='delete_task'),
    path("register/",views.User_Register,name='register'),
    path('forget/',views.Forget_Password,name='for_pass'),
    path('otp/',views.Otp_verification,name='otp'),
    path('create/' ,views.create_password ,name='create'),
    path('logout/', views.Logout_view, name='logout'),
  
]