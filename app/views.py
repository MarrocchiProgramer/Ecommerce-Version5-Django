from django.shortcuts import render
from .models import Producto
from .forms import ContactoForm

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/home.html', data)

def carrito(request):
    return render(request, 'app/carrito.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto enviado"
        else:
            data['form'] = formulario    
        
    return render(request, 'app/contacto.html', data)