"""api URL Configuration

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
from django.urls import path, include
from memorization import urls
from rest_framework.authtoken import views
from . import views as general_views

urlpatterns = [
    path('', general_views.home),
    path('admin/', admin.site.urls),
    path('memorize/', include('memorization.urls')),
    path('login/', views.obtain_auth_token),
    path('register/', general_views.create_auth)
]
