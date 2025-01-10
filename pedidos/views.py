from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pedidos.models import Pedido, DetallePedido
from carro.carro import Carro
from django.contrib import messages


@login_required(login_url="/autenticacion/logear")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    detalle_pedido=list()
    for key, value in carro.carro.items():
        detalle_pedido.append(DetallePedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
        ))

    DetallePedido.objects.bulk_create(detalle_pedido)
    
    messages.success(request, "Pedido creado correctamente")

