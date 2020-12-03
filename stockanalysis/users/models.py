from django.db import models

# Create your models here.
class SignupForm(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=10)
    