from django.shortcuts import render
from .models import Persona
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.
def personas(request):
    personas = Persona.objects.all().values()
    return JsonResponse({
        'socios': list(personas)
    })

def home(request):
    template = get_template('index.html')
    return HttpResponse(template.render())
