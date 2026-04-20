from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('api/tareas/', views.api_tareas, name='api_tareas'),
]