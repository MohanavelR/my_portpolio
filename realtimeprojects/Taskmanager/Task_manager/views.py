from django.shortcuts import render,redirect,get_object_or_404
from .forms import Login_form,Task_create_form,Register_form,Email_check,otp_check,Create_password_form
from .models import USER,Task_Create
from django.http import HttpResponse
from django.urls import reverse
from .Otp_message import Otp_generate,Send_Email
from django.contrib import messages

# ===========================Function====================
# Home_view function:--
def Home_view(request):
   try: 
    slug=request.session.get('slug')
    id=USER.objects.get(slug=slug)   
    user=Task_Create.objects.filter(User=id)
    count=len(user)
    pending=list(filter(lambda a : a.status=="Pending",user))
    complated=list(filter(lambda a : a.status=="completed",user))
    pending_count=len(pending)
    request.session['error']=''
    return render(request,'task/Home.html',{'head':'Task','data':count,'Pen_count':pending_count,'completed':len(complated)})
   except Exception as a:
     error=str(a)
     request.session['error']=error
     return redirect(reverse('Task:Login'))   
# Home_view function end  
# ========================================================================== 

def Task_view(req):
    slug=req.session.get('slug')
    id=USER.objects.get(slug=slug)
    Tasks=Task_Create.objects.filter(User=id)
    # =====================Task Create method======================== 
    if req.method=="POST":
       form=Task_create_form(req.POST)
       title=req.POST.get('title')
       descripte=req.POST.get('description')
       status=req.POST.get('status')
       User=req.session.get('id')
       if form.is_valid():
         Task_Create.objects.create(title=title,description=descripte,status=status,User_id=User)         
       else:
         return HttpResponse(form.fields)     
    return render(req,'task/Task.html',{'head':'Task','datas':Tasks})
  
def Login_view(req):
    
     if req.method=="POST":         
       form= Login_form(req.POST)
       password=req.POST.get('password')
       email=req.POST.get('email')  
       if form.is_valid():
        try:   
          get=USER.objects.get(email=email,password=password)
          req.session['slug']=get.slug
          req.session['id']=get.id
          req.session['error']='' 
          return redirect(reverse('Task:Home')) 
        except Exception as a :
          
          error="Incorrect email or password "
          messages.error(req,error)
          return redirect(reverse('Task:Login')) 
       else :
           error="Invalied  data"
           messages.error(req,error)
           return redirect( reverse('Task:Login')) 
     return render(req,'task/Login.html',{'head':'Login',}) 

def Logout_view(req):
    """
    Logout function that clears all session data and redirects to login page
    """
    # Clear all session data
    req.session.flush()
    
    # Alternative: Clear specific session keys
    # req.session.pop('slug', None)
    # req.session.pop('id', None)
    # req.session.pop('error', None)
    
    # Add success message
    messages.success(req, "You have been successfully logged out.")
    
    # Redirect to login page
    return redirect(reverse('Task:Login'))

def Task_update(req,slug):
  slugs=Task_Create.objects.get(slug=slug)
  task=get_object_or_404(Task_Create,slug=slug)
  if req.method=="POST":
       form=Task_create_form(req.POST)
       task.title=req.POST.get('title')
       task.description=req.POST.get('description')
       task.status=req.POST.get('status')
       
       if form.is_valid():
          task.save()
          return redirect(reverse("Task:task"))
  return render(req,'task/update.html',{'head':'Update','data':task})

def Delete_task(req,slug):
  task=get_object_or_404(Task_Create,slug=slug)
  task.delete()
  return redirect(reverse('Task:task')) 

def User_Register(req):
  if req.method=="POST":    
     forms=Register_form(req.POST)
     if forms.is_valid():
        forms=Register_form(req.POST)
        username=req.POST.get('username')
        email=req.POST.get('email')
        password=req.POST.get('password')
        email_in=USER.objects.filter(email=email).exists()
        if email_in:     
           error="Email is Already exsists" 
           messages.error(req,error)
           return redirect(reverse("Task:register"))
        else:    
           USER.objects.create(user_name=username,email=email,password=password)  
           return redirect(reverse('Task:Login'))
     else:
        error="Invailed Datas " 
        messages.error(req,error)
        return redirect(reverse("Task:register"))
  return render (req,'task/Register.html',{'head':'Register'})

def Forget_Password(req):
  if req.method=="POST":    
    forms1=Email_check(req.POST)
    email=req.POST.get('email')
    if forms1.is_valid():
       email_in=USER.objects.get(email=email) 
       if email_in:
         otp=Otp_generate()
         message= Send_Email(otp,email)
         req.session['otp']=otp
         req.session['email']=email
         return redirect(reverse('Task:otp'))
       else:
         return HttpResponse('not Register')
  return render(req,'task/forgetpassword.html')

def Otp_verification(req):
   user=req.session.get('otp')
   if req.method=="POST":
      forms=otp_check(req.POST)
      input_otp=req.POST.get('otp')
      if forms.is_valid():
        session_otp=req.session.get('otp')
        if int(input_otp)==session_otp:
            return redirect(reverse('Task:create'))
        else:
            return HttpResponse('unsuccess')  
   return render(req,'task/otp_verification.html',{'user':user})

def create_password(req):
  if req.method=='POST':
    forms=Create_password_form(req.POST)
    confrim_password=req.POST.get('confrim_password')
    create_password=req.POST.get('create_password')
    email=req.session.get('email')
    if forms.is_valid():
      if create_password==confrim_password:
        task=get_object_or_404(USER,email=email)
        if task:
          task.password=create_password
          task.save()
          return redirect(reverse('Task:Login'))
    
  return render(req,'task/Create_password.html')