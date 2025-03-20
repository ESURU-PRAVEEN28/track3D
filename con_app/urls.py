from django.urls import path

from .loginpage import adddata
from .views import userinput,viewdetails,sellerdetails,home
from .sendingmail import contact_view


urlpatterns=[
     path("Filters/",userinput,name="userinput"),


path('contact/', contact_view, name='contact'),
    path('viewdetails/',viewdetails,name="viewdetails"),
    path('sellerdetails',sellerdetails,name="sellerdetails"),
    path('adddata/',adddata,name="adddata"),
    path('',home,name="home"),


 ]