from django.urls import path
from . import views
app_name="blog"
urlpatterns=[
  
    # path("first_view/",views.first_view,name="first_view")
    # path('new_url_pat/',views.new_url_fun,name='new_url_name'),
    # path('old_url_pat/',views.old_url,name='old_url_name')
    path('',views.index,name="index"),
    path('details/<str:slug>',views.details,name='details'),
    path('contact/',views.Contact,name='contact'),
    path('about_us/',views.About,name="about"),
    path('register/',views.Register,name='register'),
    path('login/',views.Login,name="login"),
    path('dashboard/',views.Dashboard,name='dashboard'),
    path('logout/',views.Logout,name="logout"),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('reset_password/<uidb64>/<token>',views.Reset_Password,name='reset_password'),
    path('new_post/',views.New_post,name='new_post'),
    path('edit_post/<str:slug>',views.Edit_Post,name='edit_post'),
    path('delete_post/<str:slug>',views.Delete_post,name='delete_post'),
    path('publish_post/<str:slug>',views.Publish_post,name='publish_post'),
    
]
