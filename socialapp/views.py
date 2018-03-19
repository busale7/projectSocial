from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Posts
from .forms import PostsForm ,SignupForm, LoginForm
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def postslist(request):
	context ={
		"post" :Posts.objects.all().order_by("-Date_added"),
	}
	return render(request,"posts_list.html", context)

def signup(request):
	form =SignupForm()
	if request.method =="POST":
		form = SignupForm(request.POST)
		if form.is_valid():   #request.method =="POST":
			user =form.save(commit=False)
			user.set_password(user.password)
			user.save()
			login(request, user)
			return redirect("login")
	context ={
		"form":form
	}
	return render(request, 'signup.html', context)

def user_login(request):
	form = LoginForm()
	if request.method =="POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			authen = authenticate(username=username ,password=password)
			if authen is not None:
				login(request, authen)
				return redirect("posts_list")
	context ={
		"form":form
	}
	return render(request, 'login.html', context)


def user_logout(request):
	logout(request)
	return redirect('login')

