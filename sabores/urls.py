from django.urls import path
from .views import lista_sabores

urlpatterns = [
    path('', lista_sabores, name='lista_sabores'),
]
