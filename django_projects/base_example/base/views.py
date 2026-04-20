from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Tarea

# Create your views here.

def Home(request):
    return HttpResponse("<h1>¡Hola, Django! 👋</h1>")


def api_tareas(request):
    tareas = Tarea.objects.all().values('title', 'completed')
    return JsonResponse({"tareas": list(tareas)})