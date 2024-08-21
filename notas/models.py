from django.db import models

# Create your models here.

#creacion de la estructura BD de la aplicacion
class Nota(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.titulo}, {self.descripcion}'
