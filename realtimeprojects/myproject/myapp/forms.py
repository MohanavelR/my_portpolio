from django import forms
from django.contrib.auth.models import User 
from .models import Category,Post,About_us
from django.contrib.auth import authenticate
class ContactForm(forms.Form):
    name=forms.CharField(label='name',max_length=100,required=True)
    email=forms.EmailField(label='email',required=True)
    message=forms.CharField(label='message',required=True)
class RegisterForm(forms.ModelForm):
    username=forms.CharField(label='username',max_length=100,required=True)
    password=forms.CharField(label='password',max_length=100,required=True)
    email=forms.CharField(label='email',max_length=100,required=True)
    password_confirm=forms.CharField(label='conform password',max_length=100,required=True)
    
    class Meta:
        model=User
        fields=['username','email','password' ]
    def clean(self):
        clean_data=super().clean()
        password=clean_data.get('password')
        password_confirm=clean_data.get('password_confirm')
        if password and password_confirm and password_confirm!=password:
            raise forms.ValidationError("Passwords Doesn't Match. ") 

class LoginForm(forms.Form):
    username=forms.CharField(label='username',max_length=100)
    password=forms.CharField(label='password',max_length=100)
    def clean(self):
      clean_data=super().clean()
      username=clean_data.get('username')
      password=clean_data.get('password')
      if username and password :
          user=authenticate(username=username,password=password)
          if user is None:
              raise forms.ValidationError('Invailed Username or Password')
class Forgot_password(forms.Form):
    email=forms.CharField(label='email',max_length=100,required=True)
    def clean(self):
        clean_data= super().clean()
        email=clean_data.get('email')
        if not User.objects.filter(email=email).exists():
          raise forms.ValidationError("No User Registered with This Email")

class ResetPassword_Form(forms.Form):
    new_password=forms.CharField(label='new password',max_length=100,min_length=8)
    confirm_password=forms.CharField(label='confirm_password',max_length=100,min_length=8)

    def clean(self):
        clean_data=super().clean()
        new_password=clean_data.get('new_password')
        confirm_password=clean_data.get('confirm_password')
        if new_password and confirm_password and confirm_password!=new_password:
            raise forms.ValidationError("Passwords Doesn't Match. ") 

class Post_Form(forms.ModelForm):
    title=forms.CharField(label='title',max_length=200,required=True)
    content=forms.CharField(label='content',required=True)
    category=forms.ModelChoiceField(label='category',required=True,queryset=Category.objects.all())
    img_url=forms.ImageField(label='Image',required=False)
    
    
    class Meta:
        model=Post
        fields=[
            'title','content','category','img_url'
        ]  
    
    def clean(self):
        clean_data= super().clean()
        title=clean_data.get('title')
        content=clean_data.get('content')
        img_url=clean_data.get('img_url')
        if title and len(title)<=5:
            raise forms.ValidationError('Title is must be at least 5 charactors')
        if content and len(content)<=5:
            raise forms.ValidationError('content is must be at least 5 charactors') 
    
    def save(self,commit=...):
        post=super().save(commit)    

        clean_data= super().clean()
        img_url=clean_data.get('img_url')
        if img_url:
            post.img_url=img_url
        else:    
           img_url='default img url'
           post.img_url=img_url
        if commit:
           post.save()
        return post   
    