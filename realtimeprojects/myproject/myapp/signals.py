from django.contrib.auth.models import Group,Permission
def Groups_permission(sender ,**kwargs):
    try:
         # Create Groups
         readers,created=Group.objects.get_or_create(name="Readers")
         authors,created=Group.objects.get_or_create(name="Authors")
         editors,created=Group.objects.get_or_create(name="Editors")
         # Create Permission
         readers_permissions=[
          Permission.objects.get(codename='view_post')
         ] 
         authors_permissions=[
          Permission.objects.get(codename='add_post'),
          Permission.objects.get(codename='view_post'),
        #   Permission.objects.get(codename='change_post'),
          Permission.objects.get(codename='delete_post')
         ]
         can_publish,created=Permission.objects.get_or_create(codename='can_publish',content_type_id=7,name='can publish post')
         editors_permissions=[
          Permission.objects.get(codename='change_post'),
          Permission.objects.get(codename='view_post'),
          can_publish,
          Permission.objects.get(codename='delete_post')
         ]
         # assigning permissions
         readers.permissions.set(readers_permissions)
         authors.permissions.set(authors_permissions)
         editors.permissions.set(editors_permissions)
         print("Groups Permissions successfully")
    except Exception as e :
              print("ERROR :",str(e))