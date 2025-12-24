from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User,AbstractUser
from django.conf import settings
import datetime
# Create your models here.
# Create Slug Function
def create_slug():
     slug=datetime.datetime.now()
     return str(slug)
# ==================================================
# Create Default Delivery Date Function
def delivery_date():
     return datetime.datetime.now()+datetime.timedelta(days=5)
# ==================================================
# Product Model
class Product(models.Model):
    product_name=models.CharField(max_length=100,null=False,blank=False)
    price=models.CharField(max_length=100,blank=False,null=False)
    quantity=models.IntegerField(null=False,blank=False)
    rating=models.CharField(max_length=100)
    img_url=models.ImageField(null=True,upload_to='product/images')
    img=models.TextField(max_length=3000)
    slug=models.SlugField(blank=False,unique=True,null=False)
    is_trending=models.BooleanField(default=False)
    is_stock=models.BooleanField(default=True)
    create_at=models.DateTimeField(auto_now_add=True)
    delivery=models.IntegerField(null=True)
    offer=models.IntegerField(null=True)
    category=models.CharField(max_length=100,null=False,blank=False)
    @property
    def formatting_url(self):
          url=''
          if self.img_url:
              url=self.img_url if self.img_url.__str__().startswith(('http://','https://')) else self.img_url.url
          else:
              url=self.img  
          return url       
    def save(self,*args,**kwargs):
         self.slug=slugify(create_slug())         
         super().save(*args,**kwargs)
    def __str__(self):
        return self.product_name
# ==================================================
# Fav Product Model
class Favorites(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=False)
    create_at=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(blank=False,unique=True,null=True)
    def save(self,*args,**kwargs):
         self.slug=slugify(create_slug())
         super().save(*args,**kwargs)    
    def __str__(self):
        return self.product.product_name     
# ==================================================
# Product Order Model
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=False)
    order_at=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(blank=False,unique=True,null=True)
    is_delivered=models.BooleanField(default=False)
    on_delivery=models.DateField()
    quantity=models.IntegerField(null=False)
    def save(self,*args,**kwargs):
         self.on_delivery=delivery_date()
         self.slug=slugify(create_slug())
         super().save(*args,**kwargs)
    def __str__(self):
         return self.product.product_name
# ==================================================
# Custom User Model
class Custom_User(models.Model):
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     phone_number=models.CharField(max_length=50,null=True,blank=True)
     address=models.TextField(max_length=200,blank=True,null=True)
     slug=models.SlugField(unique=True)
     img_url=models.ImageField(null=True,upload_to='user/images')
     def image(self):
          url=self.img_url.url if self.img_url else None
          return url
     def save(self,*args,**kwargs):
          self.slug=slugify(create_slug())
          super().save(*args,**kwargs)               
# ==================================================     
     