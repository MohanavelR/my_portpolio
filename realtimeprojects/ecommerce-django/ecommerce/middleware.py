from django.shortcuts import redirect
from django.urls import reverse,resolve

# check Authenticated Path
class MiddlewareForAuthenticated:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            login_path = reverse('ecommerce:login')
            register_path = reverse('ecommerce:register')
            if request.path in [login_path, register_path]:
                return redirect(reverse('ecommerce:home'))

        response = self.get_response(request)
        return response
# ==================================================
# Check Not Authenticated path
class MiddlewareForNotAuthenticated:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        mycart_path = reverse('ecommerce:mycart')
        my_order_path=reverse('ecommerce:myorder')
        user_view_path=reverse('ecommerce:user')
        admin_view_path=reverse('ecommerce:admin')
        product_path=reverse('ecommerce:product')
        if not request.user.is_authenticated and request.path in [mycart_path,my_order_path,user_view_path,admin_view_path,product_path]:
            return redirect(reverse('ecommerce:login'))
        response = self.get_response(request)
        return response
# ==================================================
# Check Super user Path
class MiddlewareForSuperUser:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if request.user.is_superuser :
           user_view_path=reverse('ecommerce:user') 
           if request.path in [user_view_path]:
               return redirect(reverse('ecommerce:admin'))    
        response = self.get_response(request)
        return response   
# ==================================================
# Check Not Super User Path
class MiddlewareForNotSuperUser:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
      if not request.user.is_superuser:    
        admin_view_path=reverse('ecommerce:admin')
        product_view=reverse('ecommerce:product')
        product_add=reverse('ecommerce:add_product')
        product_resolve_update=resolve(request.path_info)
        product_update=product_resolve_update.url_name
        if  request.path in [admin_view_path,product_view,product_add,product_update] or product_update=='update_product' or product_update=='delete_product' :
            return redirect(reverse('ecommerce:user'))  
      response=self.get_response(request)
      return response
# ==================================================    