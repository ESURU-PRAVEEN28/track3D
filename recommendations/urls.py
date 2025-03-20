from django.urls import path
from .views import recommend_material,add,environ
from con_app.loginpage import admin_login

urlpatterns = [
    path("recommend/", recommend_material, name="recommend_material"),
path("add/", add, name="add"),
    path('environmental condition/',environ,name="environmental condition"),\
path("admin-login/", admin_login, name="admin_login"),
]
