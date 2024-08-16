from django.contrib import admin

from .models import Curso, Estudiante, Profesor, Entregable

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'comision')
    list_filter = ('nombre', 'comision')
    ordering = ("nombre",)

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('apellido'),
    list_filter = ('apellido'),
    ordering = ("apellido",)


admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Profesor)
admin.site.register(Entregable)

# Register your models here.
