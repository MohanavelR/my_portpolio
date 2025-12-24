from django.apps import AppConfig
from django.db.models.signals import post_migrate


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
    def ready(self):
       from myapp.signals import Groups_permission
       post_migrate.connect(Groups_permission)
       
