from django.shortcuts import render
from .models import Persona, Article
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.
def home(request):
    return render(request, 'index.html')

def blog_list(request):
    articles = Article.objects.all().order_by('-fecha')
    return render(request, 'blog.html', {'articles': articles})
