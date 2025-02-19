from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Producto
from django.db.models import F, Sum, FloatField

user=get_user_model()

class Pedido(models.Model):
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
    
    @property
    def total(self):
        return self.detallepedidos_set.aggregate(
            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())
        )["total"]

    class Meta:
        db_table='pedidos'
        verbose_name='pedido'
        verbose_name_plural='pedidos'
        ordering=['id']

class DetallePedido(models.Model):

    user=models.ForeignKey(user, on_delete=models.CASCADE)
    producto_id=models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido_id=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto_id.nombre}'
    
    class Meta:
        db_table='detallepedidos'
        verbose_name='detalle_pedido'
        verbose_name_plural='pedidos_detalle'
        ordering=['id']