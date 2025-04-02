from django.urls import path
from . import views

urlpatterns = [
    path('', views.hogar),
    path('api/', views.metas_path),
    path('api/<int:pk>/', views.meta_path)
]