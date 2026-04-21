from django.contrib import admin
from .models import Persona, Article

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'sexo')
    list_filter = ('nombre', 'apellido', 'dni', 'sexo', 'nacimiento', 'nacionalidad', 'direccion', 'telefono', 'correo')
    search_fields = ('nombre', 'apellido', 'dni', 'sexo', 'nacimiento', 'nacionalidad', 'direccion', 'telefono', 'correo')
    ordering = ('nombre', 'apellido', 'dni', 'sexo', 'nacimiento', 'nacionalidad', 'direccion', 'telefono', 'correo')
    

# Register your models here.
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Article)
