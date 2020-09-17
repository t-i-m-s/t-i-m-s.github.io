"""on_market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

#path('', main_page_call),
#path('registration/', include('registration.urls')),
#path('products/', include('products.urls')),
#path('check_form/', check_form, name = 'check_form'),
#path('admin/', admin.site.urls),
urlpatterns = [
    path('', include('products.urls')),
    path('admin/', admin.site.urls),
]
