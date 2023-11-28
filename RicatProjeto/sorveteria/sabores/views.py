from django.shortcuts import render
from .models import Sabor

def lista_sabores(request):
    sabores = Sabor.objects.all()
    return render(request, 'sabores/lista_sabores.html', {'sabores': sabores})
