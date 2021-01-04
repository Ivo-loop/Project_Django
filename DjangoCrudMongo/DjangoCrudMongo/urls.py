"""DjangoCrudMongo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from DjangoCrudApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_produto/', views.add_produto),
    path('update_produto/<_id>', views.update_produto),
    path('delete_produto/<_id>', views.delete_produto),
    path('read_produto/<id>', views.read_produto),
    path('read_produto_all', views.read_produto_all),
]
