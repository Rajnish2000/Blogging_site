from django.contrib import admin
from django.urls import path,include
from home import views

admin.site.site_header = 'MyCoder Admin'
admin.site.site_title = 'mycoder admin padnel'
admin.site.index_title = 'welcome to mycoder admin padnel'



urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('search/',views.search,name='search'),
    path('signUp/',views.handleSignUp,name='signUp'),
    path('login/',views.handleLogin,name='handleLogin'),
    path('logout/',views.handleLogout,name='handleLogout'), 
    path('profile/',views.profile,name='profile')    
]
