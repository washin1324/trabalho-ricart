from django.shortcuts import render
from .models import Estoque

def lista_estoque(request):
    estoque = Estoque.objects.all()
    return render(request, 'estoque/lista_estoque.html', {'estoque': estoque})
