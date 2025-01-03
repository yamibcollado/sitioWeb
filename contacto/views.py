from django.shortcuts import redirect, render
from .forms import Formulario

def contacto(request):
    formulario_contacto=Formulario()

    if request.method=="POST":
        formulario_contacto=Formulario(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            mensaje=request.POST.get("mensaje")
            
            return redirect("/contacto/?valido")

    return render(request, "contacto/contacto.html", {'formulario':formulario_contacto})

