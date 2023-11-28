from django.db import models
from sabores.models import Sabor

class Estoque(models.Model):
    sabor = models.OneToOneField(Sabor, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.sabor.nome} - {self.quantidade} unidades"
