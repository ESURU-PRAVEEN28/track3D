from django.urls import path
from .views import recommend_material,add

urlpatterns = [
    path("recommend/", recommend_material, name="recommend_material"),
path("add/", add, name="add"),

]
