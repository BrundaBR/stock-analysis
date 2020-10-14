from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserSigninForm
# Create your views here.
def Homepage(request):
    return render(request,"index.html")
def SignUp(request):
    form=UserRegisterForm()
    if request.method=='POST':
        form.save()
        redirect('/')
    form=UserRegisterForm()
    return render(request,'signup.html',{'form':form})
    
def Signin(request):
    forms=UserSigninForm()
    if request.method=='POST':
        redirect('/')
    forms=UserSigninForm()
    return render(request,'signin.html',{'forms':forms})