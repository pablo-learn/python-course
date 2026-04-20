from . import views
from django.urls import path

urlpatterns = [
    path('api/mates', views.api_mates, name="api_mates")
]