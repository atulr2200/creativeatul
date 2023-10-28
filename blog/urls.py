"""iblogs URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
   
    path('', home),
    path('about/', about),
    path('contact/',contact),
    path('login/', loginUser),
    path('logout/', logoutUser),
    path('regi/', regi),
    path('blog/<slug:url>/', post),
    path('category/<slug:url>/',category),
    path('projectSearch/',projectSearch),
    path('search/',search),
    path('projects/', show_project_page),
    path('project/<slug:title>/', projectPost),
    path('language/<int:cid>/', show_language_page),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
