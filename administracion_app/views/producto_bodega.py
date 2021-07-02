from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from producto_bodega_app.models import ProductoBodega
from producto_bodega_app.forms import ProductoBodegaForm
from django.db.models import F, Q
import random

from django.contrib.auth.decorators import permission_required, login_required



@permission_required('tienda_app.add_producto_bodega')
def admin_producto_bodega_inicio(request):
    producto_bodegas = consultar_all()
    search = request.GET.get("buscar")
    if search:
        producto_bodegas = consultar_search(search)
    data = {'producto_bodegas': producto_bodegas}
    return render(request, 'administracion_app/producto_bodega/inicio.html', data)


def admin_producto_bodega_agregar(request):
    data = {'form': ProductoBodegaForm}
    if request.method == 'POST':
        formulario = ProductoBodegaForm(data=request.POST)
        if formulario.is_valid():
            nuevo_registro = preparar_registro(formulario)
            if validar_bodega(formulario):
                nuevo_registro.save()
                messages.success(
                    request, "Ingreso de mercanciá registrado correctamente.")
                return redirect(to="admin_producto_bodega_inicio")
            else:
                messages.warning(
                    request, "El ingreso de mercancia que decea registrar excede la capacidad de la bodega.")
                data["form"] = formulario
    return render(request, 'administracion_app/producto_bodega/producto/agregar.html', data)


def admin_producto_bodega_modificar(request, uuid):
    producto_bodega = get_object_or_404(ProductoBodega, uuid=uuid)
    producto_bodegas = ProductoBodega.objects.all().annotate(
        p_ocupado=(F('capacidad_maxima') - F('capacidad_disponible')
                   )*100 / F('capacidad_maxima'),
        p_disponible=(F('capacidad_disponible')*100) / F('capacidad_maxima'),
        c_ocupada=F('capacidad_maxima') - F('capacidad_disponible'),

    )
    data = {'producto_bodegas': producto_bodegas,
            'form': ProductoBodegaForm(instance=producto_bodega)}
    if request.method == 'POST':
        formulario = ProductoBodegaForm(
            data=request.POST, instance=producto_bodega)
        if formulario.is_valid():
            formulario.save()
            messages.success(
                request, "ProductoBodega modificada correctamente.")
            return redirect(to="admin_producto_bodega_inicio")
        else:
            data["form"] = formulario
    return render(request, 'administracion_app/producto_bodega/modificar.html', data)


def admin_producto_bodega_eliminar(request, uuid):
    producto_bodega = get_object_or_404(ProductoBodega, uuid=uuid)
    producto_bodega.delete()
    messages.success(request, "ProductoBodega eliminada correctamente.")
    return redirect(to="admin_producto_bodega_inicio")


def validar_bodega(self):
    if (self.cleaned_data["bodega"].capacidad_disponible < self.cleaned_data["cantidad_entra"]):
        return False
    return True


def preparar_registro(self):
    producto_bodega = ProductoBodega()
    producto_bodega.bodega = self.cleaned_data["bodega"]
    producto_bodega.proveedor = self.cleaned_data["proveedor"]
    nombre = self.cleaned_data["nombre"].upper()
    bodega = self.cleaned_data["bodega"].nombre_corto
    pre = nombre[0:4]
    rabd = random.randint(0, 9999)
    producto_bodega.referencia = bodega + "-" + pre + "-" + \
        "{:0>3}".format(str(len(nombre))) + "-" + "{:0>4}".format(str(rabd))
    producto_bodega.nombre = nombre
    producto_bodega.costo = self.cleaned_data["costo"]
    producto_bodega.costo_unitario = self.cleaned_data["costo"] / \
        self.cleaned_data["cantidad_entra"]
    producto_bodega.cantidad_entra = self.cleaned_data["cantidad_entra"]
    producto_bodega.cantidad_minima = self.cleaned_data["cantidad_minima"]
    producto_bodega.descripcion = self.cleaned_data["descripcion"]
    return producto_bodega


def consultar_all():
    consulta = ProductoBodega.objects.all().order_by('bodega', 'proveedor', 'nombre')
    return consulta


def consultar_search(search):
    consulta = ProductoBodega.objects.filter(
        #Q(bodega__icontains=search) |
        #Q(proveedor__icontains=search) |
        Q(referencia__icontains=search) |
        Q(nombre__icontains=search) |
        Q(costo__icontains=search) |
        Q(descripcion__icontains=search)
    ).order_by('bodega', 'proveedor', 'nombre')
    return consulta
