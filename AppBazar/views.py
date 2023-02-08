from django.shortcuts import render
from AppBazar.models import *
from AppBazar.forms import *

# Create your views here.
def clientes(request):
    todos = Clientes.objects.all()
    return render (request, "AppBazar/clientes.html", {"todos":todos})

def proveedores(request):
    todos = Proveedores.objects.all()
    return render (request, "AppBazar/provedores.html", {"todos":todos})

def productos(request):
    todos = Productos.objects.all()
    return render (request, "AppBazar/productos.html", {"todos":todos})

def clientes_ver(request):
 
      if request.method == "POST":
 
            miFormulario = ClientesFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  Clientes = Clientes(nombre=informacion["nombre"], apellido=informacion["apellido"], mail=informacion["mail"])
                  clientes.save()
                  return render(request, "AppBazar/inicio.html")
      else:
            miFormulario = ClientesFormulario()
 
      return render(request, "AppBazar/clientesFormulario.html", {"miFormulario": miFormulario})
