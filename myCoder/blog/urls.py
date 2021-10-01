from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('postcomment',views.postComment,name='postComment'),
    path('', views.blogHome,name='blogHome'),
    path('<str:slug>', views.blogPost,name='blogPost'),

]
