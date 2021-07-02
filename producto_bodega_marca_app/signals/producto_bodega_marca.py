from django.db import transaction
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from producto_marca_app.models import ProductoMarca
from producto_bodega_marca_app.models import ProductoBodegaMarca


@receiver(post_save, sender=ProductoBodegaMarca)
def post_save_producto_bodega_marca(sender, instance, created, update_fields, **kwargs):
    def doit():
        producto_marca_instance = ProductoMarca.objects.get(
            uuid=instance.producto_marca_id)
        if created:
            producto_marca_instance.costo = producto_marca_instance.costo + \
                (instance.costo * instance.cantidad)
            costo = producto_marca_instance.costo
            precio =( (costo * 50) / 100 ) + costo
            utilidad = precio - costo
            producto_marca_instance.precio = precio
            producto_marca_instance.utilidad = utilidad
            producto_marca_instance.save(update_fields=('costo','precio','utilidad',))
        elif(instance.deleted_at != None):
            producto_marca_instance.costo = producto_marca_instance.costo - \
                (instance.costo * instance.cantidad)
            costo = producto_marca_instance.costo
            precio =( (costo * 50) / 100 ) + costo
            utilidad = precio - costo
            producto_marca_instance.precio = precio
            producto_marca_instance.utilidad = utilidad
            producto_marca_instance.save(update_fields=('costo','precio','utilidad',))
        else:
            update_fields
    transaction.on_commit(doit)
