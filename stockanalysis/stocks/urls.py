from django.contrib import admin
from django.urls import path,include
from stocks import views
from django.contrib.auth import views as auth_views
from users import views as a_views
urlpatterns =[
    path('',views.Homepage,name="home"),
    path('signup',a_views.SignUp,name="signup"),
    path('view/',views.View,name="view"),
    path('signin/',auth_views.LoginView.as_view(template_name='signin.html'),name='signin'),
    path('uploaddata/',views.bhav,name="upload"),
]
