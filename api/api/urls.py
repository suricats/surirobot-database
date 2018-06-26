
from django.contrib import admin
from django.urls import path, include
from memorization import urls
from rest_framework.authtoken import views
from . import views as general_views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/memorize/docs/', permanent=False), name='docs'),
    path('accounts/login/', RedirectView.as_view(url='/api-auth/login', permanent=False), name='login'),
    path('accounts/profile/', RedirectView.as_view(url='/', permanent=False), name='login'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('memorize/', include('memorization.urls')),
    path('login/', views.obtain_auth_token),
    path('register/', general_views.create_auth)
]