"""boleteria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

# AUTH_VIEW
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('cliente/', include('apps.cliente.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
    path('viaje/', include('apps.viaje.urls')),
    path('admin/', admin.site.urls),

    #PERMISSION AUTHENTICATION
    path('accounts/', include('django.contrib.auth.urls')),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
]
