from django import forms
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .models import Order,Custom_User,Product
'''

form validation is Login or check value only use 'Model' 
But Store Your data in  data base 'FormModel'
Set Class Meta into set Fields
You Want Any Check data or condition Over ride 
clean Funtion

'''
# =====================================================================
# Login Form Vaildation
class Login_form(forms.Form):
    username=forms.CharField(max_length=100,required=True)
    password=forms.CharField(max_length=100,required=True)
    def clean(self):
        data=super().clean()
        username=data.get('username')
        password=data.get('password')
        if username and password:
            user=authenticate(username=username,password=password)  
            if user is None: 
             raise forms.ValidationError('Invalied Username or Password')
# ==================================================
# Register Form Validation
# class Reigister_Phone(forms.ModelForm):
#     mobile=forms.CharField(max_length=50,required=True)
#     class Meta:
#         fields=['']
#     def clean(self):
#         data= super().clean()
#         if len(data['mobile'])!=10 :
#            raise forms.ValidationError('Please Enter Valid Mobile Number')   
# ==================================================
# Register Form Validation
class Register_form(forms.ModelForm):
    username=forms.CharField(max_length=100,required=True)
    email=forms.CharField(max_length=100,required=True)
    password=forms.CharField(max_length=100,required=True)
    re_password=forms.CharField(max_length=100,required=True)
    class Meta:
        model=User
        fields=['username','password','email']
    def clean(self):
        data= super().clean() 
        password=data.get('password')
        re_password=data.get('re_password')
        if password and password !=(re_password):
            raise forms.ValidationError("password does't Match" )
        if password and len(password)<8:
            raise forms.ValidationError('Password Must be 8 Charactors')    
# ==================================================
# Order Product Form
class Order_form(forms.ModelForm):
    quantity=forms.IntegerField(max_value=10)
    class Meta:
        model=Order
        fields=['quantity']
    def clean(self):
        data= super().clean()  
        quantity=data.get('quantity')
        if quantity<=0 :
            raise forms.ValidationError(' Please Enter Quantity ')        
# ==================================================
# Change User Details Form  vaildation
class Update_UserModel(forms.ModelForm):
    first_name=forms.CharField(max_length=100,required=False)
    last_name=forms.CharField(max_length=50,required=False)
    email=forms.CharField(max_length=50,required=False)
    class Meta:
        model=User
        fields=['first_name','last_name','email']
# ==================================================
# Custem User Form validation 
class Update_CustomUser_Model(forms.ModelForm):
    phone=forms.CharField(label='phone_number',max_length=10,required=False)
    address=forms.CharField(label='address',max_length=100,required=False)
    img_url=forms.ImageField(required=False,label='Image')
    class Meta:
        model=Custom_User
        fields=['phone_number','address','img_url']
    # def clean(self):
    #     data=super().clean() 
    #     phone=data.get('phone_number')   
    #     # if len(phone)!=10:
    #     #     raise forms.ValidationError('please Enter Vaild Phone Number')
# ==================================================
# Product Form validation
class Product_form(forms.ModelForm):
    choices=[
        ('Electronics','Electronics'),
        ('Footwear','Footwear'),
        ('Clothing','Clothing'),
        ('Furniture','Furniture'),
        ('Accessories','Accessories')
    ]
    product_name=forms.CharField(label='product_name',max_length=100,required=True)
    price=forms.CharField(label='price',required=True)
    quantity=forms.IntegerField(label='quantity',max_value=20,required=True)
    rating=forms.CharField(label='rating',max_length=100,required=True)
    offer=forms.CharField(label='offer',max_length=100,required=True)
    delivery=forms.CharField(label='delivery',max_length=100,required=True)
    category=forms.ChoiceField(required=True,choices=choices)
    img_url=forms.ImageField(required=True,label='image')
    is_trending=forms.BooleanField(label='is_trending',required=False)
    class Meta:
        model=Product
        fields=[ 
            'product_name',
            'price',
            'quantity',
            'rating',
            'is_trending',
            'img_url',
            'category',
            'offer',
            'delivery'
        ]
# ==================================================        
# ===========================================================================