from django.shortcuts import render
from .forms import Formulario

def contacto(request):
    formulario_contacto=Formulario()
    return render(request, "contacto/contacto.html", {'formulario':formulario_contacto})


