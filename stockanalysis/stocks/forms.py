from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
#user registration form with email,phone,username and password field
class UserRegisterForm(UserCreationForm):
	email=forms.EmailField()
	phone=forms.CharField(max_length=10)

	class Meta:
		model=User
		fields=['username','email','phone','password1','password2']



class UserSigninForm(UserCreationForm):
	

	class Meta:
		model=User
		fields=['username','password']