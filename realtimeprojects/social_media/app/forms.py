from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Profile,Post
from django.contrib import messages
class Login_form(forms.Form):
    username=forms.CharField(label='username',max_length=100,required=True)
    password=forms.CharField(label='password',max_length=100,required=True)
    def clean(self):
        data=super().clean()
        username=data.get('username') 
        password=data.get('password')
        if username and password :
           user=authenticate(username=username,password=password)
           if user is None:
            raise  forms.ValidationError('Invaild Username or Password')
class Signup_form(forms.ModelForm):
    username=forms.CharField(label='username',max_length=100,required=True)
    username=forms.CharField(label='email',max_length=100,required=True)
    password=forms.CharField(label='password',max_length=100,required=True)
    re_password=forms.CharField(label='re_password',max_length=100,required=True)
    class Meta:
        model=User         
        fields=['username','password','email']
    def clean(self):
        data= super().clean()    
        username=data.get('username') 
        password=data.get('password')
        re_password=data.get('re_password')
        if password and re_password and re_password!=password:
         raise forms.ValidationError("Password Don't Match")
        if password and len(password)<8:
          raise forms.ValidationError("Password Must be 8 charactors")
class Update_UserModel(forms.ModelForm):
    first_name=forms.CharField(max_length=100,required=False)
    last_name=forms.CharField(max_length=50,required=False)
    email=forms.CharField(max_length=50,required=False)
    username=forms.CharField(max_length=50,required=True)
    class Meta:
        model=User
        fields=['first_name','last_name','email','username']

class Profile_form(forms.ModelForm):
   bio=forms.CharField(max_length=500,label='bio',required=False)
   profile_img=forms.ImageField(required=False,label='profile_img')
   address=forms.CharField(max_length=500,label='address',required=False)
   mobile=forms.CharField(max_length=20,label='mobile',required=False)
   class Meta:
      model=Profile
      fields=['bio','address','profile_img','mobile']
class Post_Form(forms.ModelForm):
   image=forms.ImageField(label='image')
   caption=forms.CharField(label='caption',max_length=500,required=False)      
   class Meta:
      model=Post
      fields=[
       'image','caption'
    ]
