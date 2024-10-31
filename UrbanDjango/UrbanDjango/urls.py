"""
URL configuration for UrbanDjango project.

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
from django.urls import path
from django.views.generic import TemplateView
from example1.views import index
from task2.views import index_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),  # Это простое фунциональное представление.

    # path('index/', TemplateView.as_view(template_name='index2.html')),  # Это представление через класс
    # path('index1/', index),
    path('func/', index_task),
    path('class/', TemplateView.as_view(template_name='second_task/class_template.html')),
]
