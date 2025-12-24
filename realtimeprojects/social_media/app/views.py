from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import Login_form,Signup_form,Profile_form,Update_UserModel,Post_Form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile,Post,LikePost,Follow,Fav_post,Comment,Message,Notification
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# =========================================================
def set_last_message(username,current_user):
    obj={"msg":'',"last_message":'',"message_by_user":'','is_seen':''}
    user_messages=Message.objects.filter(sender=current_user,receiver=username).last()
    receiver_messages=Message.objects.filter(receiver=current_user,sender=username).last()  
    if user_messages and receiver_messages:           
         obj.update(msg=receiver_messages.message if user_messages.created_at < receiver_messages.created_at else user_messages.message)
         obj.update(last_message=receiver_messages.created_at if user_messages.created_at < receiver_messages.created_at else user_messages.created_at)
         obj.update(message_by_user=False if user_messages.created_at < receiver_messages.created_at else True)
         obj.update(is_seen=receiver_messages.is_seen if user_messages.created_at < receiver_messages.created_at else user_messages.is_seen)
    else:
         obj.update(msg='' if user_messages == None and receiver_messages == None else user_messages.message if receiver_messages == None else receiver_messages.message )    
         obj.update(last_message='' if user_messages == None and receiver_messages == None else user_messages.created_at if receiver_messages == None else receiver_messages.created_at)      
         obj.update(is_seen='' if user_messages == None and receiver_messages == None else user_messages.is_seen if receiver_messages == None else receiver_messages.is_seen)      
         obj.update(message_by_user=False if user_messages == None and receiver_messages == None else True if receiver_messages == None else False)      
    return obj
#======================================================================  
@login_required
def index(request):
    posts = Post.objects.all().order_by('-created_at').exclude(user=request.user)
    profiles = Profile.objects.all()
#  check is liked post
    liked_post_ids = LikePost.objects.filter(user=request.user).values_list('post__pk', flat=True)
    for post in posts:
        post.is_liked = post.pk in liked_post_ids
# ----------------------------------------------------------   
    for post in posts:
       for profile in profiles:
           if post.user.pk ==profile.user.pk:
               post.img_url=profile.profile_img.url
               post.profile_slug=profile.slug

#-------------------------------------------------------------
#   Check Following
    followings=Follow.objects.filter(user=request.user)
    for post in posts:
       for following in followings:
             if post.user.pk == following.following.pk :
               post.is_following=True
#----------------------------------------------------------------                 
    fav_post_ids = Fav_post.objects.filter(user=request.user).values_list('post__pk', flat=True)
    for post in posts:
        post.is_fav = post.pk in fav_post_ids   
#----------------------------------------------------------------                 
    for post in posts:
        comments = Comment.objects.filter(post=post).order_by('-created_at')
        post.no_of_comments=len(comments)
        comment_post_ids = comments.filter(comment_user=request.user)
        for comment in comments:
              profile =Profile.objects.get(user=comment.comment_user)
              comment.profile_slug=profile.slug
              comment.is_your_comment = comment in comment_post_ids
        post.comments = comments
#  
    return render(request,'app/index.html',{'posts':posts})
# ==================================================================================
@csrf_exempt
def search_view(request):
    users=User.objects.all().exclude(username=request.user)
    for user in users:
        profile=Profile.objects.get(user=user)
        user.image=profile.profile_img.url
        user.created_at=profile.created_at
        user.profile_slug=profile.slug
    if request.method=='POST':
        users_json=[]
        try:
            data = json.loads(request.body)
            user_name = data['data']
            if user_name !='' : 
              user_data=users.filter(username__istartswith=user_name)      
              for user in user_data:
                profile=Profile.objects.get(user=user)
                users_json.append({
                  'username':user.username,
                   'profile_slug':profile.slug,
                    'image':profile.profile_img.url
                })
            else: 
                users_json=[]
                return JsonResponse({'user':users_json})
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error': 'JSON error'}, status=400)
        return JsonResponse({'user':users_json})
    return render(request,'app/search.html',{'users':users})
# ==================================================================================
@login_required
def my_account(request):
    user_profile=Profile.objects.get(user=request.user.pk)
    posts=Post.objects.filter(user=request.user)
    followers=Follow.objects.filter(following=request.user)
    following=Follow.objects.filter(user=request.user)
    follow_user=[]
    for  i in following :
        follow_user.append(i.following)
    for follower in followers:
       profile = Profile.objects.get(user=follower.user)
       follower.img=profile.profile_img.url      
       follower.slug=profile.slug
    for follow in following:  
       profile = Profile.objects.get(user=follow.following)
       follow.img=profile.profile_img.url      
       follow.slug=profile.slug
    for follower in followers:
        follower.is_followed=follower.user in follow_user   
    context={
        'profile':user_profile,
        'posts':posts,
        "no_of_posts":len(posts),
        'following_length':len(following),
        "follower_length":len(followers),
        'following':(following),
        "followers":(followers)
        }
    return render(request,'app/user.html',context)
# ==================================================================================
@login_required
def add_post(request):
    if request.method=="POST":
        form=Post_Form(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect(reverse('app:myaccount'))
    return render(request,'app/add_post.html')
# ==================================================================================
@login_required
def like_post(request,slug):  
    post=Post.objects.get(slug=slug)
    liked_post=LikePost.objects.filter(post=post,user=request.user)
    if liked_post.exists():
        post.no_of_likes-=1
        liked_post.delete()
    else:
        post.no_of_likes+=1
        Notification.objects.create(user=post.user,sender=request.user,message=f'{request.user} Liked Your Post')
        LikePost.objects.create(post=post,user=request.user)    
    post.save()         
    return redirect(reverse('app:index'))
# ==================================================================================
@login_required
def delete_post(request,slug):
      Post.objects.get(slug=slug).delete()
      return redirect(reverse('app:myaccount'))
# ==================================================================================
@login_required
def profile_view(request,slug):
    profile=Profile.objects.get(slug=slug)
    user_detail=User.objects.get(pk=profile.user.pk)
    posts=Post.objects.filter(user=user_detail.pk)
    follower=Follow.objects.filter(following=user_detail)
    following=Follow.objects.filter(user=user_detail)
    is_following=False
    if Follow.objects.filter(user=request.user,following=user_detail).exists():
        is_following=True
    no_of_postes=len(posts)
    context={'profile':profile,
             'user_detail':user_detail,
             'posts':posts,
             'no_of_posts':no_of_postes,
               'following':len(following),
               "follower":len(follower),'is_following':is_following
             }
    return render(request,'app/profile.html',context)
# ==================================================================================
@login_required
def follow(request,slug,path):
    profile=Profile.objects.get(slug=slug)
    user_name=User.objects.get(pk=profile.user.pk)
    followed=Follow.objects.filter(following=user_name,user=request.user)
    if followed.exists():
        followed.delete()
    else :
        Follow.objects.create(following=user_name,user=request.user)
        Notification.objects.create(sender=request.user,user=user_name,message=f'{request.user} Following You ')
    return redirect(path)   
# ==================================================================================
def fav_list(request):
    posts=Fav_post.objects.filter(user=request.user)
    return render(request,'app/fav_list.html',{'posts':posts})
# ==================================================================================
def add_fav(request,slug):
    post=Post.objects.get(slug=slug)
    fav_posted=Fav_post.objects.filter(post=post,user=request.user)
    if fav_posted.exists():
        fav_posted.delete()
    else:
        Fav_post.objects.create(post=post,user=request.user)
    return redirect(reverse('app:index'))        
# ==================================================================================
def delete_fav(request,slug):
    Fav_post.objects.get(slug=slug).delete()
    return redirect(reverse('app:saved_posts')) 
# ==================================================================================
def add_comment(request):
    if request.method=='POST':
        comment=request.POST.get('comment')
        slug=request.POST.get('slug')
        post=Post.objects.get(slug=slug)
        Notification.objects.create(sender=request.user,user=post.user,message=f'{request.user} Comment Your Post :{comment}')
        Comment.objects.create(comment_user=request.user,post=post,comment=comment)
        return redirect(reverse('app:index'))
# ==================================================================================
def delete_comment(request,slug):
    Comment.objects.get(slug=slug).delete()
    return redirect(reverse('app:index'))
# ==================================================================================

@login_required
def edit_profile(request):
    user_profile=Profile.objects.get(user=request.user)
    if request.method == 'POST':
       form=Profile_form(request.POST,request.FILES,instance=user_profile)
       if form.is_valid():
           form.save()
           messages.info(request,'Successfully Updated')
           return redirect(reverse('app:edit_profile'))
           
    return render(request,'app/user_edit.html',{'profile':user_profile})
# ==================================================================================
@login_required
def edit_user(request):
    if request.method=="POST":
        user=User.objects.get(pk=request.user.pk)
        form=Update_UserModel(request.POST,instance=user)
        if form.is_valid():
            form.save()
            messages.info(request,'Successfully Updated')    
        else:
            messages.error(request,'Failed To Updated')    
    return redirect(reverse('app:edit_profile'))
# ==================================================================================
@login_required
def message_user(request,slug):
    profile=Profile.objects.get(slug=slug)
    user_messages=Message.objects.filter(sender=request.user,receiver=profile.user,is_delete=False)
    receiver_messages=Message.objects.filter(sender=profile.user,receiver=request.user)
    messages=[]
    for message in user_messages:
        message.is_message_by_user=True
        messages.append(message)
    for message in receiver_messages:
        message.is_seen=True
        message.save()            
        message.is_message_by_user=False
        messages.append(message) 
    messages.sort(key=lambda x:x.created_at)
    
    if request.method=="POST":
         print(request.path)
         message=request.POST.get('message')
         Notification.objects.create(sender=request.user,user=profile.user,message=f'{request.user} Messaged You : {message}')
         Message.objects.create(sender=request.user,receiver=profile.user,message=message)
         return redirect(request.path)
    return render(request,'app/message.html',{'profile':profile,'messages':messages})

# ==================================================================================
def delete_message(request,slug,path):
    message=Message.objects.filter(slug=slug).first()
    message.is_delete=True
    message.save()
    return redirect(path)
# ==================================================================================

@login_required
def message_view(request):
    user_messages=Message.objects.filter(sender=request.user)
    receiver_messages=Message.objects.filter(receiver=request.user)
    username_set=set()
    for message in user_messages:
        username_set.add(message.receiver.username)
    for message in receiver_messages :
        username_set.add(message.sender.username)
    user_list=[]
    for user in username_set:
        get_username=User.objects.get(username=user)
        profile=Profile.objects.get(user=get_username)
        get_all_unseen=Message.objects.filter(receiver=request.user,sender=get_username,is_seen=False).count()
        obj=set_last_message(get_username,request.user)  
        user_list.append({"username":user,'count':get_all_unseen,"slug":profile.slug,"img":profile.formatting_url,'obj':obj})    
    user_list.sort(key= lambda x:x['obj']['last_message'],reverse=True)

    return render(request,'app/messager.html',{'users':user_list})
# ==================================================================================
@login_required(login_url='/login/')
def notification_view(request):
    notifications=Notification.objects.filter(user=request.user).order_by('-created_at')
    for notify in notifications:
        profile=Profile.objects.get(user=notify.sender)
        notify.user_slug=profile.slug
        notify.img=profile.formatting_url
        notify.is_seen=True   
        notify.save()
        
    return render(request,'app/notification.html',{'notifications':notifications})
# ==================================================================================
@login_required
def delete_notify(request,slug):
    Notification.objects.get(slug=slug).delete()
    return redirect(reverse('app:notification'))
def sign_in(request):
    form=Login_form()
    if request.method=="POST":
       form=Login_form(request.POST)
       if form.is_valid():
           username=form.cleaned_data.get('username')
           password=form.cleaned_data.get('password')
           user=authenticate(username=username,password=password)
           if user is not None:
               login(request,user)
               return redirect(reverse('app:index'))
    return render(request,'authentication/login.html',{'form':form})
# ==================================================================================

def sign_up(request):
    form=Signup_form()
    if request.method=="POST":
       form=Signup_form(request.POST)
       if form.is_valid():
           user=form.save(commit=False)
           password=form.cleaned_data.get('password')
           user.set_password(password)
           
           user.save()
           messages.info(request,'Successfully Register')
           Profile.objects.create(user=user)
           return redirect(reverse('app:login'))
    return render(request,'authentication/signup.html',{'form':form})
# ==================================================================================
@login_required
def logout_process(request):
    logout(request)
    return redirect(reverse('app:login'))