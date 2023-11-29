from django.urls import path
from . import views

urlpatterns = [
  path('clientes/', views.cliente_list, name='clientes'),
  path('clientes/adicionar', views.cliente_add, name='adicionar_cliente'),
  path('sabores/', views.sabor_list, name='sabores'),
  path('pedidos/', views.pedido_list, name='pedidos'),
  path('estoque/', views.estoque_list, name='estoque'),
  path('', views.home_page, name='home_page'),
]