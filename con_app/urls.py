from django.urls import path

from .loginpage import adddata
from .views import userinput,viewdetails,sellerdetails
from .sendingmail import contact_view


urlpatterns=[
     path("",userinput,name="userinput"),


path('contact/', contact_view, name='contact'),
    path('viewdetails/',viewdetails,name="viewdetails"),
    path('sellerdetails',sellerdetails,name="sellerdetails"),
    path('adddata/',adddata,name="adddata")

 ]