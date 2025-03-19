from django.db import models

# Create your models here.

class Student(models.Model):
    nom = models.CharField(max_length=100)
    cognom1 = models.CharField(max_length=100)
    cognom2 = models.CharField(max_length=100, blank=True, null=True)
    correu = models.EmailField()
    curs = models.CharField(max_length=50)
    moduls_matriculats = models.TextField()

class Teacher(models.Model):
    nom = models.CharField(max_length=100)
    cognom1 = models.CharField(max_length=100)
    cognom2 = models.CharField(max_length=100, blank=True, null=True)
    correu = models.EmailField()
    curs = models.CharField(max_length=50)
    tutor = models.BooleanField(default=False)
    moduls_imparteix = models.TextField()