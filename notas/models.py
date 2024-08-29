from django.db import models

# Create your models here.

# creacion de la estructura BD de la aplicacion


class Nota(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=200)
    creado = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.titulo
