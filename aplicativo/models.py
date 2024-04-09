from django.db import models

# Create your models here.

class Usuarios(models.Model):
    id_usuarios = models.AutoField(primary_key=True)
    nome = models.TextField(255)
    email = models.TextField(255)
    setor = models.TextField(255)
