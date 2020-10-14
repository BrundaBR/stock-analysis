from django.contrib import admin
from django.urls import path,include
from stocks import views
from django.contrib.auth import views as auth_views
urlpatterns =[
    path('',views.Homepage,name="home"),
    path('signup',views.SignUp,name="signup"),
    path('signin',views.Signin,name='signin'),
]