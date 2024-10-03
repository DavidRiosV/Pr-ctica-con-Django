from django.shortcuts import render
from .models import Animal,Protectora,Colaborador

# Create your views here.
def animal_list(request):
    animal=Animal.objects.all()
    return render(request, 'Animales/Animal_list.html',{'animal_mostrar':animal})

def protectora_list(request):
    protectora=Protectora.objects.all()
    return render(request, 'Animales/Protectora_list.html',{'protectora_mostrar':protectora})

def colaborador_list(request):
    colaborador=Colaborador.objects.all()
    return render(request, 'Animales/Colaborador_list.html',{'colaborador_mostrar':colaborador})