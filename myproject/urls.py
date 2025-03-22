"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from restaurants_app.models import RestaurantReview
from users.views import register_user, user_profile
from restaurants_app.views import review_create, review_list, review_detail

def home(request):
    latest_reviews = RestaurantReview.objects.all().order_by('-id')[:6]
    return render(request, 'home.html', {
        'latest_reviews': latest_reviews
    })

def about(request):
    return render(request, 'about.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    
    # Web URLs
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='home'
    ), name='logout'),
    path('register/', register_user, name='register'),
    path('profile/', user_profile, name='profile'),
    
    # Restaurant review URLs
    path('reviews/', review_list, name='review_list'),
    path('reviews/<int:pk>/', review_detail, name='review_detail'),
    path('post/', review_create, name='post'),
]
