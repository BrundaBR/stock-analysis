from django.shortcuts import render,redirect

from .forms import UserRegisterForm
# Create your views here.

def SignUp(request):
	if request.method=="POST":
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			
			return redirect('home')

	else:
        
		form=UserRegisterForm()
        

	return render(request,'signup.html',{'form':form})