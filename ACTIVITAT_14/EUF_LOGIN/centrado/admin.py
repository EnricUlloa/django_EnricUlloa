from django.contrib import admin
from .models import Usuario
from django.contrib.auth.hashers import make_password

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'nombre', 'apellido')

#Aqui tuve que preguntar a una ia ya que no lograba solucionar el problema de la contraseña.
    def save_model(self, request, obj, form, change):
        if not change or 'password' in form.changed_data:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)
