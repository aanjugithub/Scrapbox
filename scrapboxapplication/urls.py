"""
URL configuration for scrapboxapplication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from scrapbox import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',views.RegistrationView.as_view(),name="register"),
    path('signin',views.LoginView.as_view(),name="signin"),
    path('index',views.IndexView.as_view(),name="index"),
    path('scrap/create',views.ScrapCreateView.as_view(),name="scrap-create"),
    path('signout',views.SignOutView.as_view(),name="signout"),
    path('listall',views.ScrapboxListView.as_view(),name="list-all"),
    path('itemview/<int:pk>/viewdetails',views.ItemView.as_view(),name="itemview"),
    path('profile/<int:pk>/view',views.ProfileDetailView.as_view(),name="profiledetail_view"),
   
    
    
]


 