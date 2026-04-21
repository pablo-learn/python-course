from django.urls import path
from . import views

urlpatterns = [
    path('api/socios', views.personas, name='personas'),
    path('', views.home, name='home'),
]