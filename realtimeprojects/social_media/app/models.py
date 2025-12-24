from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify 
import random
import datetime
def random_str():
 create_string=''
 str='qwertyuiopasdfghjklzxcvbnm1234567890'
 for i in range(1,20):
  create_string+=str[random.randint(0,29)]
 return create_string
#============================  
def create_slug():
   date=datetime.datetime.today()
   return str(date)+random_str()
# =====================================
class Profile(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   profile_img=models.ImageField(upload_to='profile/images',null=True,default='profile/default_img.png')
   bio=models.TextField(blank=True,default='Your bio goes here... 👋🏽')
   address=models.TextField(blank=True)
   mobile=models.CharField(max_length=20,blank=True,null=True)
   slug=models.SlugField(unique=True)
   created_at=models.DateTimeField(auto_now_add=True)
   def save(self,*args,**kwargs):
      self.slug=create_slug()
      return super().save(*args,**kwargs)
   '''
   
   '''
   @property
   def formatting_url(self):
          url=self.profile_img if self.profile_img.__str__().startswith(('http://','https://')) else self.profile_img.url
          return url  
   def __str__(self):
      return self.user.username
class Post(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   image=models.ImageField(upload_to='posts/images')
   caption=models.TextField(null=True,blank=True)
   slug=models.SlugField(unique=True)
   created_at=models.DateTimeField(auto_now_add=True)
   no_of_likes=models.IntegerField(default=0)
   def save(self,*args,**kwargs):
      self.slug=slugify(create_slug())
      return super().save(*args,**kwargs)  
   def __str__(self):
       return self.user.username+str(self.pk)+str(self.caption)
class LikePost(models.Model):
   post=models.ForeignKey(Post,on_delete=models.CASCADE)
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   def __str__(self):
       return self.user.username     
class Follow(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    def __str__(self):
       return (str(self.user.username)+'following'+str(self.following))
class Comment(models.Model):
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    comment=models.TextField(null=False,blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE ) 
    slug =models.SlugField(unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def save(self,*args,**kwargs):
      self.slug=slugify(create_slug())
      return super().save(*args,**kwargs)
    def __str__(self):
       return str(self.comment_user.username)+' commented this user post '+str(self.post.user)
class Fav_post(models.Model):
   post = models.ForeignKey(Post, on_delete=models.CASCADE )
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   slug=models.SlugField(unique=True)
   created_at=models.DateTimeField(auto_now_add=True) 
   def save(self,*args,**kwargs):
      self.slug=slugify(create_slug())
      return super().save(*args,**kwargs)
   def __str__(self):
      return self.user.username 
class Message(models.Model):
   sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')   
   receiver=models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver')
   message=models.TextField(null=False,blank=False)
   slug=models.SlugField(unique=True)
   created_at=models.DateTimeField(auto_now_add=True) 
   is_delete=models.BooleanField(default=False)
   is_seen=models.BooleanField(default=False)
   def save(self,*args,**kwargs):
      self.slug=slugify(create_slug())
      return super().save(*args,**kwargs)
   def __str__(self):
      return f'{self.sender} message {self.receiver}'
class Notification(models.Model):
   message=models.CharField(max_length=200)
   user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
   slug=models.SlugField(unique=True)
   sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='another')   
   created_at=models.DateTimeField(auto_now_add=True) 
   is_seen=models.BooleanField(default=False)
   def save(self,*args,**kwargs):
      self.slug=slugify(create_slug())
      return super().save(*args,**kwargs)
   def __str__(self):
      return f'{self.message}'      
