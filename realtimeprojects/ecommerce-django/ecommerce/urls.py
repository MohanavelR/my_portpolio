from django.urls import path
from . import views

# 
app_name='ecommerce'
urlpatterns=[
   path('',views.home,name="home"),   
   path('shopping/',views.shopping,name='shopping'),
   path('details/<str:slug>',views.detail,name='detail'),
   path('login/',views.login_view,name='login'),
   path('register/',views.register,name='register'),
   path('logout/',views.Logout_view,name='logout'),
   path('mycart/',views.my_cart,name="mycart"),
   path('add_cart/<int:id>', views.add_card,name='add_cart'),
   path('delete_cart/<str:slug>',views.delete_cart,name='delete_cart'),
   path('myorder/',views.my_order,name='myorder'),
   path('delete_order/<str:slug>',views.delete_order,name='delete_order'),
   path('product/',views.product_view,name='product'),
   path('add_product/',views.add_product,name='add_product'),
   path('admin_view/',views.admin_view,name="admin"),
   path('user_view/', views.user_view ,name="user"),
   path('update_product/<str:slug>',views.update_product,name='update_product'),
   path('delete_product/<str:slug>',views.delete_product,name='delete_product')

]