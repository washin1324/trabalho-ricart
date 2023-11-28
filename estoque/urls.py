from django.urls import path
from .views import lista_estoque

urlpatterns = [
    path('estoque/', lista_estoque, name='lista_estoque'),
]
