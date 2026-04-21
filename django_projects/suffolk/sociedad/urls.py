from django.urls import path
from . import views

urlpatterns = [
    path('api/socios', views.personas, name='personas'),
    path('blog/', views.blog_list, name='blog_list'),
    path('', views.home, name='home'),
]