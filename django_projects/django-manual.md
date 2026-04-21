# Guía Rápida: Crear un Endpoint en Django

Esta guía se enfoca exclusivamente en los pasos necesarios para definir datos, administrarlos desde el panel de Django y exponerlos a través de un endpoint JSON.

## 1. Definir el Modelo
Crea la estructura de tus datos en `models.py`.

```python
from django.db import models

class MiModelo(models.Model):
    titulo = models.CharField(max_length=100)
    # Agrega más campos si es necesario

    def __str__(self):
        return self.titulo
```

## 2. Migraciones y Base de Datos
Cada vez que cambies el modelo, debes sincronizar la base de datos.

```bash
# 1. Preparar las instrucciones de cambio
python manage.py makemigrations

# 2. Aplicar los cambios a la base de datos
python manage.py migrate
```

## 3. Acceso al Admin
Para poder agregar datos visualmente, necesitas un superusuario y registrar el modelo.

**Crear superusuario:**
```bash
python manage.py createsuperuser
```

**Registrar en `admin.py`:**
```python
from django.contrib import admin
from .models import MiModelo

admin.site.register(MiModelo)
```
> [!TIP]
> Accede a `http://127.0.0.1:8000/admin/` para agregar registros.

## 4. Crear el Endpoint (Vista JSON)
Define la lógica para devolver los datos en `views.py`.

```python
from django.http import JsonResponse
from .models import MiModelo

def api_endpoint(request):
    # .values() convierte los objetos en diccionarios
    datos = MiModelo.objects.all().values()
    return JsonResponse({
        "data": list(datos)
    })
```

## 5. Configurar URLs
Conecta tu vista a una dirección web.

**En el `urls.py` de tu aplicación:**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('api/datos/', views.api_endpoint, name='api_datos'),
]
```

**En el `urls.py` del proyecto (carpeta principal):**
```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tu_app.urls')), # Reemplaza 'tu_app' por el nombre de tu app
]
```

## Verificación
1. Inicia el servidor: `python manage.py runserver`
2. Agrega datos en `/admin/`
3. Visita `/api/datos/` para ver el JSON.
