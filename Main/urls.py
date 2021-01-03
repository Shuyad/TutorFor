from django.contrib import admin
from django.urls import path
from Main import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('support',views.support,name='support'),
    path('user/login',views.login,name='login'),
    path('user/signup',views.signup,name='signup'),
    path('user/forgotPassword',views.forgotPassword,name='forgotPassword'),
    path('user/dashboard',views.dashboard,name='dashboard'),
]
