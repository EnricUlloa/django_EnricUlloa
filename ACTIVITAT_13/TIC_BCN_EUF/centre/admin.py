from django.contrib import admin
from .models import Student, Teacher

# Register your models here.

@admin.register(Student)
class Alumnes(admin.ModelAdmin):
    list_display = ('nom', 'cognom1', 'cognom2', 'correu', 'curs', 'moduls_matriculats')

@admin.register(Teacher)
class Professor(admin.ModelAdmin):
    list_display = ('nom', 'cognom1', 'cognom2', 'correu', 'curs', 'tutor', 'moduls_imparteix')