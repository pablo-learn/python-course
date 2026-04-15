# Guía de Inicio Rápido con Django

Esta guía te ayudará a configurar tu primer proyecto de Django paso a paso. Sigue estos comandos en tu terminal.

## Paso 1: Configuración del Entorno Virtual

Es una buena práctica trabajar dentro de un entorno virtual para no mezclar las librerías de diferentes proyectos.

```bash
# Crear el entorno virtual
python3 -m venv venv

# Activar el entorno virtual
source venv/bin/activate
```

## Paso 2: Instalación de Django

Una vez activado el entorno, instala Django usando `pip`.

```bash
pip install django
```

## Paso 3: Crear el Proyecto y la Aplicación

Django organiza el código en "Proyectos" (la configuración global) y "Aplicaciones" (funcionalidades específicas).

```bash
# Crear el proyecto llamado 'core'
django-admin startproject core .

# Crear una aplicación llamada 'base'
python manage.py startapp base
```

## Paso 4: Configuración Inicial

Ahora debemos registrar la nueva aplicación en el archivo de configuración del proyecto.

1. Abre `core/settings.py`.
2. Busca la lista `INSTALLED_APPS`.
3. Añade `'base',` al final de la lista.

## Paso 5: Tu Primera Vista (Hola Mundo)

Vamos a crear una vista simple que devuelva texto.

1. Abre `base/views.py` y añade:

    ```python
    from django.http import HttpResponse

    def home(request):
        return HttpResponse("<h1>¡Hola, Django! 👋</h1>")
    ```

2. Crea un archivo `base/urls.py` y añade:

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.home, name='home'),
    ]
    ```

3. Modifica `core/urls.py` para incluir las rutas de la aplicación:

    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('base.urls')), # ¡Asegúrate de usar punto, no barra!
    ]
    ```

## Paso 6: Crear un Superusuario (Root)
Para acceder al panel de administración de Django, necesitas un usuario con permisos.

1. Ejecuta las migraciones iniciales para crear las tablas de base de datos necesarias:
   ```bash
   python manage.py migrate
   ```

2. Crea el superusuario:
   ```bash
   python manage.py createsuperuser
   ```
   Sigue las instrucciones en la consola (nombre de usuario, email y contraseña).

## Paso 7: Crear un Modelo y Migraciones
Un "Modelo" es la representación de una tabla en tu base de datos.

1. Abre `base/models.py` y añade un modelo sencillo:
   ```python
   from django.db import models

   class Tarea(models.Model):
       title = models.CharField(max_length=200)
       completed = models.BooleanField(default=False)

       def __str__(self):
           return self.title
   ```

2. **MUY IMPORTANTE:** Genera y aplica los cambios. Django necesita primero *analizar* los cambios (`makemigrations`) y luego *aplicarlos* (`migrate`).
   ```bash
   # 1. Crear el archivo de migración (instrucciones)
   python manage.py makemigrations base

   # 2. Aplicar los cambios a la base de datos real
   python manage.py migrate
   ```

## Paso 8: Registrar en el Admin
Para poder agregar datos desde la interfaz de Django, debes registrar el modelo.

1. Abre `base/admin.py` y añade:
   ```python
   from django.contrib import admin
   from .models import Tarea

   admin.site.register(Tarea)
   ```

> [!TIP]
> Ahora puedes entrar a `http://127.0.0.1:8000/admin`, loguearte con tu superusuario y verás que puedes agregar "Tareas".

## Paso 9: Crear una API Sencilla (JSON)
Vamos a crear una ruta que devuelva los datos de tus tareas en formato JSON.

1. En `base/views.py`, añade una nueva vista:
   ```python
   from django.http import JsonResponse
   from .models import Tarea

   def api_tareas(request):
       # .values() debe llevar paréntesis y los nombres de los campos del modelo
       tareas = Tarea.objects.all().values('title', 'completed')
       return JsonResponse({"tareas": list(tareas)})
   ```

2. En `base/urls.py`, registra la ruta de la API:
   ```python
   urlpatterns = [
       path('', views.Home, name='home'),
       path('api/tareas/', views.api_tareas, name='api_tareas'),
   ]
   ```

## Verificación Final
- [x] ¿Usaste `'base.urls'` en `core/urls.py`?
- [ ] ¿Ejecutaste `makemigrations` Y `migrate`?
- [ ] ¿Aparecen las "Tareas" en el admin?
- [ ] ¿`http://127.0.0.1:8000/api/tareas/` devuelve el JSON correcto?
