from django.shortcuts import render, redirect
from .models import Cliente, Sabor, Pedido, Estoque
from .forms import ClienteForm


# Create your views here.
def home_page(request):
  return render(request, 'home_page.html')

def cliente_list(request):
  return render(request, 'clientes.html', {'clientes': Cliente.objects.all()})

def cliente_add(request):
  if request.method == 'POST':
    form = ClienteForm(request.POST)
    
    if form.is_valid():
      form.save()
      return redirect('/sorveteria')
    
    else:
      return render(request, 'adicionar_cliente.html', {'form': form})
    
  return render(request, 'adicionar_cliente.html', {'form': ClienteForm()})

def sabor_list(request):
  return render(request, 'sabores.html', {'sabores': Sabor.objects.all()})

def pedido_list(request):
  return render(request, 'pedidos.html', {'pedidos': Pedido.objects.all()})

def estoque_list(request):
  return render(request, 'estoque.html', {'estoque': Estoque.objects.all()})