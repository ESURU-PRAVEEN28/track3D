from django.urls import path
from .views import userinput


urlpatterns=[
     path("",userinput,name="userinput"),
 ]