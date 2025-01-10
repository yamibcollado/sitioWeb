from django.contrib import admin

from .models import Pedido, DetallePedido

admin.site.register([Pedido, DetallePedido])