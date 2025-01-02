from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, "webApp/home.html")

def tienda(request):
    return render(request, "webApp/tienda.html")

def contacto(request):
    return render(request, "webApp/contacto.html")
