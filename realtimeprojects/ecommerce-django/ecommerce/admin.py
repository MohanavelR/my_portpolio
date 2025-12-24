from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Favorites,Product,Order,Custom_User
# Register your models here.

# add Django admin 
admin.site.register(Custom_User)    
admin.site.register(Favorites)
admin.site.register(Product)
admin.site.register(Order)