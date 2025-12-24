from django.contrib import admin
from .models import Post,Category,About_us

# Register your models here.
 

class Post_admin(admin.ModelAdmin):
    list_display=('title','content')
    search_fields=('title','content')
    list_filter=('category','create_at')
admin.site.register(Post,Post_admin)
admin.site.register(Category)
admin.site.register(About_us)