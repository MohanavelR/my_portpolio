from django import forms

class Login_form(forms.Form):
    email=forms.EmailField(label='email',required=True)
    password=forms.CharField(label='password', required=True)
class Task_create_form(forms.Form):
    title=forms.CharField( label='title',max_length=200,required=True) 
    description=forms.CharField(label='description', max_length=1000,required=True)
    status=forms.CharField(label='status',required=True)
class Register_form(forms.Form):
    email=forms.EmailField(label='email',required=True)
    password=forms.CharField(label='password', required=True)
    username=forms.CharField(label='username',required=True)
class Email_check(forms.Form):
    email=forms.EmailField()  
class otp_check(forms.Form):
    otp=forms.CharField(max_length=20) 
class Create_password_form(forms.Form):
    create_password=forms.CharField(label='create_password', required=True)
    confrim_password=forms.CharField(label='confrim_password',required=True)