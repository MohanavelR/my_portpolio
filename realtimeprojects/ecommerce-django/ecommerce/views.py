from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from .models import Product,Favorites,Order,Custom_User
from django.contrib import messages
from .forms import Login_form,Register_form,Order_form,Update_UserModel,Update_CustomUser_Model,Product_form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
# Create your views here.

# Function of Home page
def home(request):
  all_product=Product.objects.filter(is_trending=True)
  if request.user.is_authenticated:
        product_id  = Favorites.objects.filter(user=request.user)
        user_fav_products =[item.pk for item in all_product  for item2 in product_id if item.pk==item2.product.pk]
        for product in all_product:
            product.is_favourited = product.id in user_fav_products
  else:
        for product in all_product:
            product.is_favourited = False
         
  return render(request,'content/home.html',{"products":all_product})
# ===================================================================

def detail(request,slug):
  form=Order_form()
  get_product=Product.objects.get(slug=slug)
  all_product=Product.objects.filter(category=get_product.category)
  if request.user.is_authenticated:
        product_id  = Favorites.objects.filter(user=request.user)
        user_fav_products =[item.pk for item in all_product  for item2 in product_id if item.pk==item2.product.pk]
        for product in all_product:
            product.is_favourited = product.id in user_fav_products
  else:
        for product in all_product:
            product.is_favourited = False    
  if request.method=="POST":
      form=Order_form(request.POST)
      if form.is_valid():
          quantity=form.cleaned_data['quantity'] 
          Order.objects.create(user_id=request.user.pk,product_id=get_product.pk,quantity=quantity)
          return redirect(reverse('ecommerce:myorder'))         
  return render(request,'content/details.html',{'products':all_product,"get_product":get_product,"form":form})  
# ===================================================================


def shopping(request):
  all_product=Product.objects.all() 
  if request.user.is_authenticated:
        product_id  = Favorites.objects.filter(user=request.user)
        user_fav_products =[item.pk for item in all_product  for item2 in product_id if item.pk==item2.product.pk]  
        # Add a custom attribute to each product
        for product in all_product:
            product.is_favourited = product.id in user_fav_products
 
  else:
        for product in all_product:
            product.is_favourited = False                               
  return render(request,'content/shopping.html',{"products":all_product})  
# ===================================================================


@login_required
def my_cart(request):
   product_id=Favorites.objects.filter(user=request.user)
   all_product=Product.objects.all()
  #  products=[item for item in all_product  for item2 in product_id if ]
   products=[]
   for product in all_product:
       for fav in product_id:
          if product.pk==fav.product.pk :
              product.fav_slug=fav.slug
              product.is_favourited = True
              products.append(product)
   return render(request,'content/mycart.html',{'products':products})
# ===================================================================


@login_required
def add_card(request,id):
   Favorites.objects.create(user_id=request.user.pk,product_id=id)
   return redirect(reverse('ecommerce:mycart'))
# ===================================================================


@login_required
def delete_cart(request,slug):
    Favorites.objects.get(slug=slug).delete()
    return redirect(reverse('ecommerce:mycart'))
# ===================================================================


@login_required
def my_order(request):
    get_all_product=Product.objects.all()
    order_items=Order.objects.filter(user=request.user)
    products = []
    for item in get_all_product:
      for item2 in order_items:
        if item.pk == item2.product.pk:
            item.on_delivery = item2.on_delivery
            item.order_at = item2.order_at
            item.quantity=item2.quantity
            item.is_delivered = item2.is_delivered
            item.order_id=item2.pk
            item.order_slug=item2.slug
            products.append(item)
    
    #  products=[(item.objects.update({'on_delivery':item2.on_delivery,"order_at":item2.order_at,"is_delivered":item2.is_delivered})) for item in get_all_product for item2 in order_items if item.pk==item2.product.pk]
    return render(request,'content/order.html',{'products':products})   
# ===================================================================


@login_required
def delete_order(request,slug):
    Order.objects.get(slug=slug).delete()
    return redirect(reverse('ecommerce:myorder'))
# ===================================================================


@login_required
def product_view(request):
  products=Product.objects.all()
  return render(request,'admin/product.html',{'products':products})
# ===================================================================


@login_required
def add_product(request):
    form=Product_form()
    if request.method=="POST":
        form=Product_form(request.POST,request.FILES)
        
        if form.is_valid():
           form.save()
           return redirect(reverse('ecommerce:product'))
    return render(request,'admin/add_product.html',{'form':form})
# ===================================================================


@login_required
def update_product(request,slug):
    product=Product.objects.get(slug=slug)  
    form=Product_form()
    if request.method=="POST":
        form=Product_form(request.POST,request.FILES,instance=product)
        if form.is_valid():
           form.save()
           return redirect(reverse('ecommerce:product'))
    return render(request,'admin/update_product.html',{'product':product})
# ===================================================================


@login_required
def delete_product(request,slug):
    Product.objects.get(slug=slug).delete()
    return redirect(reverse('ecommerce:product'))
# ===================================================================

@login_required
def admin_view(request):
    data=User.objects.get(pk=request.user.pk)
    data_2=Custom_User.objects.get(user=request.user)
    users=User.objects.all()
    total_product=len(Product.objects.all())
    total_order=len(Order.objects.all())
    total_user=len(users)
    form=Update_CustomUser_Model()
    if request.method=="POST":
        form=Update_CustomUser_Model(request.POST,request.FILES,instance=data_2)
        form_2=Update_UserModel(request.POST,instance=data)
        if form.is_valid():
            if form_2.is_valid():
                form.save()
                form_2.save()
    data.phone_number=data_2.phone_number
    data.address=data_2.address
    data.total_product=total_product
    data.total_order=total_order
    data.total_user=total_user  
    data.url=data_2.image()
    return render(request,'admin/admin.html',{'data':data,'users':users})
# ===================================================================
@login_required
def user_view(request):
    form=Update_CustomUser_Model()
    data=User.objects.get(pk=request.user.pk)
    data_2=Custom_User.objects.get(user=request.user)
    get_all_product=Product.objects.all()
    order_items=Order.objects.filter(user=request.user)
    products = []
    for item in get_all_product:
      for item2 in order_items:
        if item.pk == item2.product.pk:
            item.on_delivery = item2.on_delivery
            item.order_at = item2.order_at
            item.quantity=item2.quantity
            item.is_delivered = item2.is_delivered
            item.order_id=item2.pk
            item.order_slug=item2.slug
            item.url=item.img_url
            products.append(item)
    if request.method=='POST':
        form=Update_CustomUser_Model(request.POST,request.FILES,instance=data_2)
        form_2=Update_UserModel(request.POST,instance=data)
        if form.is_valid:
           if form_2.is_valid: 
              form.save()
              form_2.save()
    data.phone_number=data_2.phone_number
    data.address =data_2.address
    data.url=data_2.image()                      
    return render(request,'login/user.html',{'data':data,'form':form,'products':products})
# ===================================================================


def login_view(request):
  form=Login_form()   
  if request.method=='POST':
    form= Login_form(request.POST)
    if form.is_valid():
        user_name=form.cleaned_data['username']
        password=form.cleaned_data['password']
        user=authenticate(username=user_name,password=password)
        if user is not None:
            login(request,user)
        return redirect(reverse('ecommerce:home'))     
  return render(request,'login/login.html',{"form":form})
# ===================================================================


def register(request):
  form=Register_form()
  if request.method=="POST":
    form=Register_form(request.POST)
    if form.is_valid():
      # username=form.cleaned_data['username']
      # email=form.cleaned_data['email']
      password=form.cleaned_data['password']
      user=form.save(commit=False)
      user.set_password(password)
      user.save()
      Custom_User.objects.create(user=user,phone_number='',address='')
      messages.success(request,'Successfully Registered')
      return redirect(reverse('ecommerce:login'))
  return render(request,'login/register.html',{'form':form})
# ===================================================================

def Logout_view(request):
   logout(request)
   return redirect(reverse('ecommerce:home'))
