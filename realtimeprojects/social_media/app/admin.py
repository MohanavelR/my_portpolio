from django.contrib import admin
from .models import LikePost,Post,Profile,Follow,Fav_post,Comment,Message,Notification

# Register your models here.
admin.site.register(LikePost)
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Follow)
admin.site.register(Fav_post)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(Notification)
