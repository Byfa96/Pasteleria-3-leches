from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from apps.shop.models import Pastel
from .serializers import PastelSerializer, PruebaSerializer
from .models import Prueba
from .forms import PruebaForm

class PastelViewSet(viewsets.ModelViewSet):
    queryset = Pastel.objects.all()

#Se crea el viewset de pruebas junto con la vista de prueba, para
# confirmar que funca el metodo de las url para crear css personalizado

class PruebaViewSet(viewsets.ModelViewSet):
    queryset = Prueba.objects.all()
    serializer_class = PruebaSerializer

def prueba_create(request):
    pruebas = Prueba.objects.all()

    if request.method == 'POST':
        form = PruebaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prueba_create')
    else:
        form = PruebaForm()
    
    return render(request, 'prueba_create.html', {'form': form, 'pruebas': pruebas})

def prueba_update(request, pk):
    prueba = get_object_or_404(Prueba, pk=pk)
    if request.method == 'POST':
        form = PruebaForm(request.POST, innstance=prueba)
        if form.is_valid():
            form.save()
            return redirect('prueba_create')
    else:
        form = PruebaForm(instance=prueba)
    
    return render(request, 'prueba_form.html', {'form': form, 'prueba': prueba})

def prueba_delete(request, pk):
    prueba = get_object_or_404(Prueba, pk=pk)
    prueba.delete()
    return redirect('prueba_create')

