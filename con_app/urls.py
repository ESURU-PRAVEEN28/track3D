from django.urls import path
from .views import userinput,custom_admin_login


urlpatterns=[
     path("",userinput,name="userinput"),
path('admin/login/', custom_admin_login, name='custom_admin_login'),
 ]