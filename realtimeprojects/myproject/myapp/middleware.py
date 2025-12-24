from django.urls import reverse
from django.shortcuts import redirect
class RediractAuthendicateUserMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self, request):
            # Check the User Authenticated
            if request.user.is_authenticated :
                #  List path check
                path_to_redirect=[
                     reverse('blog:login'),
                     reverse('blog:register'),
                ]
                if request.path in path_to_redirect:
                     return redirect(reverse('blog:index'))    
            response=self.get_response(request)    
            return response
class RediractNotAuthendicateUserMiddleware :
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self, request):
        path_to_redirect=[
                     reverse('blog:dashboard'),
                     
                ]  
        if not request.user.is_authenticated and request.path in path_to_redirect:
             return redirect(reverse('blog:login'))
        
        response=self.get_response(request)
        return response 