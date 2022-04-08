from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('errors/', views.errors, name='errors'),
    path('label/', views.label, name='label'),
    path('admin/', admin.site.urls),
]
