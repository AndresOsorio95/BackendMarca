from django.shortcuts import redirect, render, get_object_or_404
from django.urls.conf import include
from django.db.models import F, Sum, Count, Q
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from producto_marca_app.models import ProductoMarca
from producto_bodega_marca_app.models import ProductoBodegaMarca
from producto_bodega_marca_app.forms import ProductoBodegaMarcaForm
from producto_bodega_app.models import ProductoBodega, producto_bodega


def admin_producto_bodega_marca_agregar(request, uuid):
    producto_marca = get_object_or_404(ProductoMarca, uuid=uuid)
    producto_bodegas = consultar_producto_bodega_all()
    search = request.GET.get("buscar")
    if search:
        producto_bodegas = consultar_producto_bodega_search(search)
    detalles = ProductoBodegaMarca.objects.filter(producto_marca=producto_marca).values(
        'producto_marca').annotate(
            producto_marca_uuid=F('producto_marca__uuid'),
            producto_bodega_referencia=F('producto_bodega__referencia'),
            producto_bodega_uuuid=F('producto_bodega__uuid'),
            producto_bodega=F('producto_bodega__nombre'),
            cantidad=Sum('cantidad'),
            costo=Sum('costo')).order_by('producto_bodega')
    data = {'producto_marca': producto_marca, 'producto_bodegas': producto_bodegas,
            'detalles': detalles, 'form': ProductoBodegaMarcaForm}
    return render(request, 'administracion_app/producto_marca/detalle/agregar.html', data)


def admin_producto_bodega_marca_eliminar_detalle_(request, producto_bodeg_uuid, producto_marca_uuid):
    producto = ProductoBodegaMarca.objects.filter(
        producto_bodega__uuid=producto_bodeg_uuid, producto_marca__uuid=producto_marca_uuid)
    producto[0].delete()
    messages.success(request, "Articulo removido.")
    return redirect(to="admin_producto_bodega_marca_agregar", uuid=producto_marca_uuid)


def admin_producto_bodega_marca_agregar_detalle(request, uuid_bodega, uuid_marca):
    producto_bodega = get_object_or_404(ProductoBodega, uuid=uuid_bodega)
    producto_marca = get_object_or_404(ProductoMarca, uuid=uuid_marca)
    nuevo_registro = preparar_registro(producto_bodega, producto_marca)
    nuevo_registro.save()
    messages.success(request, 'Articulo agregao exitosamente.')
    return redirect(to="admin_producto_bodega_marca_agregar", uuid=uuid_marca)


def preparar_registro(producto_bodega, producto_marca):
    producto_bodega_marca = ProductoBodegaMarca()
    producto_bodega_marca.producto_bodega = producto_bodega
    producto_bodega_marca.producto_marca = producto_marca
    producto_bodega_marca.cantidad = 1
    producto_bodega_marca.costo = producto_bodega.costo_unitario
    return producto_bodega_marca


def consultar_producto_bodega_all():
    consulta = ProductoBodega.objects.filter(
        is_relacionado=True).order_by('bodega', 'proveedor', 'nombre')
    return consulta


def consultar_producto_bodega_search(search):
    consulta = ProductoBodega.objects.filter(
        Q(costo_unitario__icontains=search) |
        Q(referencia__icontains=search) |
        Q(nombre__icontains=search) |
        Q(costo__icontains=search) |
        Q(descripcion__icontains=search),
        is_relacionado=True
    ).order_by('bodega', 'proveedor', 'nombre')
    return consulta
