from django.db import models
from django.db.models.base import Model


class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    cuit = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)


class Pagina(models.Model):
    titulo = models.CharField(max_length=255)
    sub_titulo = models.TextField()
    descripcion = models.TextField()
    tipo = models.CharField(max_length=255)


class Secciones(models.Model):
    nombre = models.CharField(max_length=40)
    titulo = models.CharField(max_length=255)
    sub_titulo = models.TextField()
    descripcion = models.TextField()
    imagen = models.CharField(max_length=255)
    pagina = models.ForeignKey(
        Pagina, on_delete=models.CASCADE, related_name='secciones'
    )

