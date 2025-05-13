from django.db import models

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    password = models.CharField(max_length=128, null=False)
