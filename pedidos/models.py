from django.db import models
from sabores.models import Sabor
from clientes.models import Cliente

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    sabores = models.ManyToManyField(Sabor)
    data_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente.nome} - {self.data_pedido}"
