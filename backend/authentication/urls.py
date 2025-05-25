from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.api_home, name="api_home"),
    path('signup',views.api_signup, name="api_signup"),
    path('signin',views.api_signin, name="api_signin"),
    path('signout',views.api_signout, name="api_signout"),
]
