from django.db import transaction
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from producto_bodega_app.models import *
from bodega_app.models import Bodega


@receiver(post_save, sender=ProductoBodega)
def post_save_producto_bodega(sender, instance, created, update_fields, **kwargs):
    def doit():
        if created:
            bodega_instance = Bodega.objects.get(uuid=instance.bodega_id)
            bodega_instance.capacidad_disponible = bodega_instance.capacidad_disponible - instance.cantidad_entra
            bodega_instance.save(update_fields=('capacidad_disponible',))
        elif (instance.deleted_at != None):
            bodega_instance = Bodega.objects.get(uuid=instance.bodega_id)
            bodega_instance.capacidad_disponible = bodega_instance.capacidad_disponible + instance.cantidad_disponible
            bodega_instance.save(update_fields=('capacidad_disponible',))

        else:
            update_fields

    transaction.on_commit(doit)