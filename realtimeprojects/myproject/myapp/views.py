from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.http import HttpResponse,Http404
from .models import Post,Category,About_us
from django.core.paginator import Paginator
from .forms import ContactForm, LoginForm,RegisterForm,Forgot_password ,ResetPassword_Form,Post_Form
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
# from django.core.mail.backends.smtp import EmailBackend
# Create your views here.

def first_view(req):
    return HttpResponse('<h1 align="center" style="background-color:blue;color:white ;padding:20px">Welcome to Python in Django...<h1>')

# def old_url(req):
#     return redirect(reverse('blog:new_url_name'))
# def new_url_fun(req):
#     return HttpResponse("I am old urls")
# posts=[
#     {"id":1,"title":"post 1",'contant':'this is post 1'},
#     {"id":2,"title":"post 2",'contant':'this is post 2'},
#     {"id":3,"title":"post 3",'contant':'this is post 3'},
#     {"id":4,"title":"post 4",'contant':'this is post 4'},
#     {"id":5,"title":"post 5",'contant':'this is post 5'},
# ]
def index(req):
    all_posts = Post.objects.all().order_by('-create_at')
    pages = Paginator(all_posts, 5)
    page_number=req.GET.get('page')
    page_of_posts=pages.get_page(page_number)
    
    return render(req,'blog/index.html',{"posts":page_of_posts})
def details(req,slug):
    if req.user  and not  req.user.has_perm('myapp.view_post'): 
       messages.error(req,'You have no permissions to view any Post') 
       return redirect(reverse("blog:index"))
    try:
       post=Post.objects.get(slug=slug)
       related_posts=Post.objects.filter(category=post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post Does Not Exist!")
    # post=next((post for post in posts if post['id']==post_id),None )
    return render(req,'blog/details.html',{"post":post,'related_post':related_posts})

def Contact(req):
    if req.method=='POST':
        form_value=ContactForm(req.POST)
        name=req.POST.get('name')
        email=req.POST.get('email')
        message=req.POST.get('message')
        if form_value.is_valid():
           success="Successfully Submited." 
           return render(req,'blog/contact.html',{'messages':success})        
        #    return HttpResponse(form_value.cleaned_data['name'])
        else:
         
          return render(req,'blog/contact.html',{'form':form_value,'name':name,'email':email,'message':message})
    return render(req,'blog/contact.html')
def About(req):
    content=About_us.objects.first()
    if content is None or not content.content  :
        content="default content"
    else:
       content=content.content
    return render(req,'blog/about.html',{'content':content})
def Register(req):
    form_value=None
    if req.method=="POST":
        form_value=RegisterForm(req.POST)
        user_name=req.POST.get('username')
        password=req.POST.get('password')
        email=req.POST.get('email')
      #   confirm_password=req.POST.get('password_confirm')
        if form_value.is_valid():
           user=form_value.save(commit=False)
           user.set_password(password)
           user.save()
         #   add default groups
           reader_group,created=Group.objects.get_or_create(name='Readers')
           user.groups.add(reader_group) 
           messages.success(req,'Registraction Successfully ')
           return redirect(reverse("blog:login"))
        #    return render(req,'authantication/register.html')  
        else:
           print('successfully failed.')
           return render(req,'authantication/register.html',{"form":form_value})
    return render(req,'authantication/register.html',{"form":form_value})
def Login(req):
    form_value=LoginForm()
    if req.method=="POST":
     form_value=LoginForm(req.POST)
     if form_value.is_valid():
      user_name=form_value.cleaned_data['username']
      password=form_value.cleaned_data['password']
      user=authenticate(username=user_name,password=password)
      if user is not None:
         login(req,user)
         print('login success')
         return redirect(reverse("blog:dashboard"))
     else :
        print() 
    return render(req,'authantication/login.html',{'form':form_value})
def Dashboard(req):
   current_user_posts=Post.objects.filter(user=req.user)
   pages=Paginator(current_user_posts,5)
   page_number=req.GET.get('page')
   page_of_posts=pages.get_page(page_number)
   title="My posts"
   return render(req,'authantication/dashboard.html',{'title':title,'posts':page_of_posts})
def Logout(req):
    logout(req)
    return redirect(reverse("blog:index"))
def forgot_password(req):
    form_value=None
    if req.method=="POST":
       form_value=Forgot_password(req.POST)
       if form_value.is_valid():
          email=form_value.cleaned_data['email']
          user=User.objects.get(email=email)
          token=default_token_generator.make_token(user)
          u_id=urlsafe_base64_encode(force_bytes(user.pk))
          site=get_current_site(req)
          subject='Reset Password Requested'
          domain=site.domain
          print("----------------------------------")
          print("----------------------------------")
          print('uid :',u_id)
          print('token :',token)
          print('domain:',domain)   
          print("----------------------------------")
          print("----------------------------------")      
          message=render_to_string('authantication/reset_email_password.html',{
             'domain':domain,
             'uid':u_id,
             'token':token
             })


          send_mail(subject=subject,message=message,from_email="noreply@mohan.com",recipient_list=[email]) 
          messages.success(req,"Email has been sent") 
          pass
   
    return render(req,'authantication/forgot_password.html',{'form':form_value})
def Reset_Password(req,uidb64,token):
   form_value=None
   if req.method=="POST":
      form_value=ResetPassword_Form(req.POST)
      if form_value.is_valid():
         new_password=req.POST.get('new_password')
         try:
           uid=urlsafe_base64_decode(uidb64)
           user=User.objects.get(pk=uid)
         except (TypeError,ValueError,OverflowError,User.DoesNotExist):
            user=None
         if user is not None and default_token_generator.check_token(user,token):
            user.set_password(new_password)
            user.save()
            messages.success(req,"Your Password has been Reset Successfully !")
            return redirect(reverse('blog:login'))   
         else:
            messages.error(req,'The Reset Link is Invailed') 


   return render(req,'authantication/reset_password',{'form':form_value})

# Post CRUD Function
@login_required
@permission_required('myapp.add_post',raise_exception=True)
def New_post(req):
   category=Category.objects.all()
   form_value=None
   if req.method=="POST":
      form_value=Post_Form(req.POST,req.FILES)
      if form_value.is_valid():
         post=form_value.save(commit=False)
         post.user=req.user
         post.save()
         return redirect(reverse("blog:dashboard"))
      pass
   return render(req,'blog/new_post.html',{'category':category,'form':form_value})
@login_required
def Edit_Post(req,slug):
     category=Category.objects.all()
     post=get_object_or_404(Post,slug=slug)
     form_value=None
     if req.method=="POST":
        form_value=Post_Form(req.POST,req.FILES,instance=post)
        if form_value.is_valid():
           form_value.save()
           messages.success(req,'Succefully Updated')
           return redirect(reverse("blog:dashboard"))
     return render(req,'blog/edit_post.html',{'category':category,'post':post,'form':form_value})
@login_required
def Delete_post(req,slug):
      post=get_object_or_404(Post,slug=slug)
      post.delete()
      messages.success(req,'Succefully Deleted')
      return redirect(reverse("blog:dashboard"))
@login_required
@permission_required('myapp.can_publish',raise_exception=True)
def Publish_post(req,slug):
      post=get_object_or_404(Post,slug=slug)
      print("post :",post)
      print("-------------------------------")
      if(post.is_published==True):
         post.is_published=False
         post.save()
         messages.success(req,'UnPuplished successfully ')
      elif(post.is_published==False):
         post.is_published=True
         post.save()
         messages.success(req,'Puplished successfully ')
      return redirect(reverse("blog:dashboard"))