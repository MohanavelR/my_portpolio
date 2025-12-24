from django.shortcuts import redirect
from django.urls import reverse,resolve

class MiddlewareforAuthenticated:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
         if request.user.is_authenticated:
              login=reverse('app:login')
              signup=reverse('app:signup')
              if request.path in [login,signup]:
               return redirect(reverse('app:index'))
         response=self.get_response(request)
         return response        
class MiddlewareforNotAuthenticated:
     def __init__(self,get_response):
          self.get_response=get_response
     def __call__(self, request):
         if not request.user.is_authenticated:
             index=reverse('app:index')
             search=reverse('app:search')
             myaccount=reverse('app:myaccount')
             add_post=reverse('app:add_post')
             edit_user=reverse('app:edit_user')
             add_comment=reverse('app:add_comment')
             saved_posts=reverse('app:saved_posts')
             message=reverse('app:message_view')
             notification=reverse('app:notification')
             path_name=resolve(request.path_info).url_name
             if request.path in [index,search,myaccount,edit_user,add_post,add_comment,saved_posts,message,notification] or path_name=='like_post' or  path_name=='delete_post' or path_name=='profile' or path_name== 'follow' or path_name=='add_fav' or path_name== 'delete_fav' or path_name=='delete_comment' or path_name=='message':
                 return redirect(reverse('app:login'))
         response=self.get_response(request)
         return response       