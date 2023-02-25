
from django.urls import path
from AppBazar.views import *

urlpatterns = [
    path('clientes/', clientes),
    path('verclientes/', clientes_ver),
    path('verclientes/', clientes_ver, name="crearCliente"),
]
