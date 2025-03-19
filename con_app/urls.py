from django.urls import path
from .views import userinput,custom_admin_login,viewdetails
from .sendingmail import contact_view


urlpatterns=[
     path("",userinput,name="userinput"),
path('admin/login/', custom_admin_login, name='custom_admin_login'),

path('contact/', contact_view, name='contact'),
    path('viewdetails/',viewdetails,name="viewdetails")

 ]