from django.shortcuts import render
from .models import Persona
from django.http import JsonResponse

# Create your views here.
def personas(request):
    personas = Persona.objects.all().values()
    return JsonResponse({
        'socios': list(personas)
    })
