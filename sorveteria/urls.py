from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sabores.urls')),
    path('', include('clientes.urls')),
    path('', include('pedidos.urls')),
    path('', include('estoque.urls')),
]
