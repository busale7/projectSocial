from django.shortcuts import render, redirect
from django.http import JsonResponse ,Http404 , HttpResponse
from .models import Posts, favorit,profile
from .forms import PostsForm ,SignupForm, LoginForm
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def testing(request,user_id):
	context ={
	"tests":Posts.objects.get(id=user_id),
	"profiles":profile.objects.get(id=user_id),


	}
	return render(request,"test.html", context)

'''def user_detail(request,user_id):
	user_obj=User.objects.get(id=user_id)'''

def postslist(request):
	if request.user.is_anonymous:
		return redirect('login')
	object_list = Posts.objects.all().order_by('Date_added')
	query= request.GET.get('q')
	if query:
		object_list=object_list.filter(author__username__icontains=query) #for searching /filtering the authors
	
	liked_posts=[]
	likes=request.user.favorit_set.all()
	for like in likes: 
		liked_posts.append(like.story)
	
	context={
		"posts": object_list,
		"my_likes": liked_posts,

	}
	return render(request,"posts_list.html", context)


'''def postslist(request):
	context ={
		"post" :Posts.objects.all().order_by("-Date_added"),
	}
	return render(request,"posts_list.html", context)'''

def creat_post(request):
	'''if not (request.user.is_staff or request.user.is_superuser):
								return HttpResponse("<h1> AMIGO YOU CANT ACCESS the page!</h1>")'''

	form =PostsForm(request.POST or None, request.FILES or None)
	if form.is_valid():

		post=form.save(commit=False)
		post.author=request.user
		post.save()
		messages.success(request,"Successfully Created")
		return redirect('posts_list')

	context ={
		"create_form":form

	}
	return render(request, "create_post.html", context)

def delete_post(request,post_id):
	if not (request.user.is_staff or request.user.is_superuser):
		return HttpResponse("<h1> AMIGO YOU CANT delete this posts only admins</h1>")
	Posts.objects.get(id=post_id).delete()
	return redirect("posts_list")

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

def like(request, post_id):
	favorit_obj = Posts.objects.get(id=post_id)
	buz_obj, created = favorit.objects.get_or_create(user=request.user, story=favorit_obj)
	if created :
		action="favorit"
	else: 
		action="Not favorit"
		buz_obj.delete()
	
	favorit_count = favorit_obj.favorit_set.all().count()

	#message="HEllo"
	context={
		#"message": message 
		"action":action,
		"count":favorit_count,


	}
	return JsonResponse(context,safe=False)

def user_profile(request,profile_id):
	user = User.objects.get(id=profile_id)
	context ={
	"profiles":profile.objects.get(user_name=user),

	}
	return render(request,"profile.html", context)


