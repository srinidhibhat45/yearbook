from django.urls import path
from gallery import views

urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
    path('photo/<str:pk>', views.photo, name='photo'),
    path('add/', views.add, name='add'),
]