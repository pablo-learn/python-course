from django.shortcuts import render
from django.http import JsonResponse
from .models import Mates

# Create your views here.
def api_mates(request):
    # mates = Mates.objects.all().values
    tareas = Mates.objects.all().values()

    return JsonResponse({
         "response": list(tareas)
    })