"""socialproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from socialapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.postslist, name="posts_list"),
    path('signup/',views.signup, name="signup_list"),
    path('login/',views.user_login, name="login"),
    path('logout/',views.user_logout, name="logout"),
    path('create/',views.creat_post, name="creat_post"),
    path('delete/<int:post_id>/', views.delete_post, name='delete'),
    path('like/<int:post_id>',views.like, name="like-button"),
    path('test/<int:user_id>',views.testing, name="test"),
    path('profile/<int:profile_id>',views.user_profile, name="profilee"),
    


]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
