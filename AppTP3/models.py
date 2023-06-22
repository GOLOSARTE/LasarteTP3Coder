from django.db import models

# Create your models here.

class Curso (models.Model):
    nombre = models.CharField(max_length=20)
    camada = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} / Camada: {self.camada}"
    

class Alumno (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} / Apellido: {self.apellido}"
    
class Profesor (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    materia = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} / Materia: {self.materia}"



