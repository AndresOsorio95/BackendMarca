from django.db.models.fields import files
from django.shortcuts import redirect, render, get_object_or_404
from django.urls.conf import include
from django.db.models import F, Sum, Count
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from producto_marca_app.models import ProductoMarca
from producto_bodega_marca_app.models import ProductoBodegaMarca
from imagen_producto_marca_app.models import ImagenProductoMarca
from imagen_producto_marca_app.forms import ImagenProductoMarcaForm


def admin_producto_bodega_marca_agregar_imagen(request, uuid):
    producto_marca = get_object_or_404(ProductoMarca, uuid=uuid)
    detalles = ProductoBodegaMarca.objects.filter(producto_marca=producto_marca).values(
        'producto_marca').annotate(
            producto_marca_uuid=F('producto_marca__uuid'),
            producto_bodega_referencia=F('producto_bodega__referencia'),
            producto_bodega_uuuid=F('producto_bodega__uuid'),
            producto_bodega=F('producto_bodega__nombre'),
            cantidad=Sum('cantidad'),
            costo=Sum('costo')).order_by('producto_bodega')
    imagens = ImagenProductoMarca.objects.filter(producto_marca=producto_marca)
    data = {'producto_marca': producto_marca, 'detalles': detalles,
            'imagens': imagens, 'form': ImagenProductoMarcaForm()}
    if request.method == 'POST':
        formulario = ImagenProductoMarcaForm(
            data=request.POST, files=request.FILES)
        if formulario.is_valid():
            nuevo_registro = preparar_registro(formulario, producto_marca)
            nuevo_registro.save()
            messages.success(request, "Imagen agregada correctramente.")
    return render(request, 'administracion_app/producto_marca/imagen/agregar.html', data)


def admin_producto_bodega_marca_listar_imagen(request, uuid):
    producto_marca = get_object_or_404(ProductoMarca, uuid=uuid)
    detalles = ProductoBodegaMarca.objects.filter(producto_marca=producto_marca).values(
        'producto_marca').annotate(
            producto_marca_uuid=F('producto_marca__uuid'),
            producto_bodega_referencia=F('producto_bodega__referencia'),
            producto_bodega_uuuid=F('producto_bodega__uuid'),
            producto_bodega=F('producto_bodega__nombre'),
            cantidad=Sum('cantidad'),
            costo=Sum('costo')).order_by('producto_bodega')
    imagens = ImagenProductoMarca.objects.filter(producto_marca=producto_marca)
    images = preparar_imagens(imagens)
    data = {'producto_marca': producto_marca, 'detalles': detalles,
            'imagens': images}
    return render(request, 'administracion_app/producto_marca/producto/ver_detallado.html', data)


def admin_producto_bodega_marca_eliminar_detalle(request, producto_bodeg_uuid, producto_marca_uuid):
    producto = ProductoBodegaMarca.objects.filter(
        producto_bodega__uuid=producto_bodeg_uuid, producto_marca__uuid=producto_marca_uuid)
    producto[0].delete()
    messages.success(request, "Articulo removido.")
    return redirect(to="admin_producto_bodega_marca_listar_imagen", uuid=producto_marca_uuid)


def admin_producto_bodega_marca_eliminar(request, uuid):
    imagen = get_object_or_404(ImagenProductoMarca, uuid=uuid)
    imagen.delete()
    producto_marca = imagen.producto_marca
    messages.success(request, "Imagen removida correctamente.")
    return redirect(to="admin_producto_bodega_marca_agregar_imagen", uuid=producto_marca.uuid)


def preparar_registro(self, producto_marca):
    imagen = ImagenProductoMarca()
    imagen.producto_marca = producto_marca
    imagen.imagen = self.cleaned_data["imagen"]
    return imagen


def preparar_imagens(self):
    lista = []
    p = 0
    for i in self:
        imagen = ImagenProductoMarca()
        imagen.uuid = i.uuid
        imagen.producto_marca = i.producto_marca
        imagen.imagen = i.imagen
        if p == 0:
            imagen.primera = True
        lista.append(imagen)
        p = p+1
    return lista
