from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, "webApp/home.html")

def tienda(request):
    return render(request, "webApp/tienda.html")


