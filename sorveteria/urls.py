from django.urls import path
from . import views

urlpatterns = [
  path('sorveteria/clientes/', views.cliente_list_request_handler, name='clientes'),
  path('sorveteria/clientes/adicionar', views.cliente_add_handler, name='adicionar_cliente'),
  path('sorveteria/sabores/', views.sabor_request_handler, name='sabores'),
  path('sorveteria/pedidos/', views.pedido_request_handler, name='pedidos'),
  path('sorveteria/estoque/', views.estoque_request_handler, name='estoque'),
  path('', views.home_page_handler, name='home_page'),
]