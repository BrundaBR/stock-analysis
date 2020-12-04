from django.contrib import admin
from django.urls import path,include
from stocks import views
from django.contrib.auth import views as auth_views
from users import views as a_views
urlpatterns =[
    path('',views.Homepage,name="home"),
    path('signup',a_views.SignUp,name="signup"),
    path('view/',views.View,name="view"),
    path('signin/',a_views.Signin,name="signin"),
    path('uploaddata/',views.bhav,name="upload"),
    path('analysis/',views.analysis,name='analysis'),
    path('filter_trades/',views.filter_trades_1000,name='filter_trades'),
    path('filter_trades_max/',views.filter_max_trades,name='filter_trades_max'),
]
