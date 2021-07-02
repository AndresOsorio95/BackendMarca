import uuid
from django.db import transaction
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from producto_bodega_app.models import *
from producto_bodega_detalle_app.models import *


@receiver(post_save, sender=ProductoBodegaDetalle)
def post_save_producto_bodega_detalle(sender, instance, created, update_fields, **kwargs):
    def doit():
        producto_bodega_instance = ProductoBodega.objects.get(uuid=instance.producto_bodega_id)
        if created:
            producto_bodega_instance.cantidad_disponible = producto_bodega_instance.cantidad_disponible + 1
            producto_bodega_instance.save(update_fields=('cantidad_disponible',))
            if producto_bodega_instance.cantidad_disponible == producto_bodega_instance.cantidad_entra:
                producto_bodega_instance.is_relacionado = True
                producto_bodega_instance.save(update_fields=('is_relacionado',))
        elif(instance.deleted_at != None):
            producto_bodega_instance.cantidad_disponible = producto_bodega_instance.cantidad_disponible - 1
            producto_bodega_instance.save(update_fields=('cantidad_disponible',))
        else:
            update_fields
    transaction.on_commit(doit)
