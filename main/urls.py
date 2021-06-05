from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('join/', views.join, name='join'),
]