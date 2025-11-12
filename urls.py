"""
URL configuration for zoo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.display_zoo1,name="MYSORE ZOO"),
    path('sec/',views.display_sec,name="jungle"),
    path('tiger/',views.display_tiger,name="TIGER"),
    path('lion/',views.display_lion,name="LION"),
    path('orangutan/',views.display_orangutan,name="ORANGUTAN"),
    path('zebra/',views.display_zebra,name="ZEBRA"),
    path('leopard/',views.display_leopard,name="leopard"),
    path('animals/',views.animal_data,name="Animal Data"),
    path('login/',views.login,name="login endpoint"),
    path('zoos/',views.zoo_data,name="zoos endpoint"),
    path('booking/',views.book_ticket,name="book endpoint"),
]
