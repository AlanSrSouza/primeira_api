from django.db import models

class Biblioteca(models.Model):
    titulo = models.CharField(max_length=20)
    autor = models.CharField(max_length=20)
    valor = models.CharField(max_length=20)
