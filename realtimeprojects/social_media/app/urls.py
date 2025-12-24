from django.urls import path
from . import views
app_name='app'
urlpatterns=[
   path('',views.index,name='index'),
   path('login/',views.sign_in,name='login'),
   path('myaccount/',views.my_account,name='myaccount'),
   path('search/',views.search_view,name='search'),
   path('myaccount_edit',views.edit_profile,name='edit_profile'),
   path('add_post/',views.add_post,name='add_post'),
   path('delete_post/<str:slug>',views.delete_post,name='delete_post'),
   path('edit_user/',views.edit_user,name='edit_user'),
   path('like_post/<str:slug>',views.like_post,name='like_post'),
   path('profile/<str:slug>',views.profile_view,name='profile'),
   path('follow/<str:slug>/<path:path>',views.follow,name='follow'),
   path('saved_posts/',views.fav_list,name='saved_posts'),
   path('add_fav/<str:slug>',views.add_fav,name='add_fav'),
   path('delete_fav/<str:slug>',views.delete_fav,name='delete_fav'),
   path('add_comment/',views.add_comment,name='add_comment'),
   path('message/',views.message_view,name='message_view'),
   path('notification/',views.notification_view,name='notification'),
   path('delete_notify/<str:slug>',views.delete_notify,name='delete_notify'),
   path('message/<str:slug>',views.message_user,name='message'),
   path('delete_message/<str:slug>/<path:path>',views.delete_message,name='delete_message'),
   path('delete_comment/<str:slug>',views.delete_comment,name='delete_comment'),
   path('signup/',views.sign_up,name='signup'),
   path('logout/',views.logout_process,name='logout'),
]