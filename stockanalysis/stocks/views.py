from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserSigninForm
# Create your views here.
def Homepage(request):
    return render(request,"index.html")