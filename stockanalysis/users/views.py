from django.shortcuts import render,redirect
from .models import SignupForm
from django.contrib.auth import authenticate
# Create your views here.

user=[]
def SignUp(request):
	if request.method=="POST":
		username_data=request.POST.get('username')
		email_data=request.POST.get('email')
		password_data=request.POST.get('password')
# save data from user to form

		save_data=SignupForm(username=username_data,email=email_data,password=password_data)
		save_data.save()
	
		return redirect('/signin')
	else:
		return render(request,'signup.html')
		
def Signin(request):
	if user!=[]:user.pop()
	if request.method=="POST":
		user_name=request.POST.get('username')
		password_data=request.POST.get('password')
		if SignupForm.objects.filter(username=user_name,password=password_data):
			user.append(user_name)
			return redirect('/home')
		else:
			return redirect('/signup')
	return render(request,'signin.html')

def signout(request):
	return render(request,'signout.html')
