from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')
def ofertas(request):
    return render(request, 'ofertas.html')

def computadoras(request):
    return render(request, 'computadoras.html')

def laptops(request):
    return render(request, 'laptops.html')

def teclados(request):
    return render(request, 'teclados.html')

def mouse(request):
    return render(request, 'Mouses.html')