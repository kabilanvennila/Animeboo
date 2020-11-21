from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.main,name="main"),
    path('home/',views.home.as_view(),name="home"),
    path('home/add/',views.add_post.as_view(),name="add"),
    path('home/<int:pk>/',views.Individual.as_view(),name="Individual"),
    path('home/update/<int:pk>/',views.update_post.as_view(),name="update"),
    path('myposts/',views.myposts,name="myposts"),
    path('myposts/delete',views.delete_post.as_view(),name="delete"),
]