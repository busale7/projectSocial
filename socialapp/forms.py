from django import forms
from django.core.files.images import get_image_dimensions

from .models import Posts #importing the class Business from models.py
from django.contrib.auth.models import User #importing User from models



class PostsForm(forms.ModelForm):
	class Meta: 
		model=Posts
		fields=['title', 'Details', 'image']
		widgets= {
			"add_date" : forms.DateInput(attrs={"type":"date"})
		}

class SignupForm(forms.ModelForm):
	class Meta: 
		model =User
		fields =['username','email','first_name','last_name', 'password']
		widgets={
			"password" : forms.PasswordInput()

		}

class LoginForm(forms.Form):
	username= forms.CharField(required=True)
	password =forms.CharField(required=True, widget=forms.PasswordInput())
	
