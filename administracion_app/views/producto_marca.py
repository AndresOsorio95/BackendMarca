from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages
from django.db.models import Q
import random
from producto_marca_app.models import ProductoMarca
from producto_marca_app.forms import ProductoMarcaForm


def admin_producto_marca_inicio(request):
    producto_marcas = consultar_all()
    search = request.GET.get("buscar")
    if search:
        producto_marcas = consultar_search(search)
    data = {'producto_marcas': producto_marcas}
    return render(request, 'administracion_app/producto_marca/inicio.html', data)


def admin_producto_marca_agregar(request):
    data = {'form': ProductoMarcaForm}
    if request.method == 'POST':
        fomrulario = ProductoMarcaForm(data=request.POST)
        if fomrulario.is_valid():
            nuevo_registro = preparar_registro(fomrulario)
            nuevo_registro.save()
            messages.success(request, "Producto MARCA creado correctamente")
            return redirect(to="admin_producto_marca_inicio")
        else:
            data["form"] = fomrulario
    return render(request, 'administracion_app/producto_marca/producto/agregar.html', data)


def preparar_registro(self):
    producto_marca = ProductoMarca()
    producto_marca.seccion = self.cleaned_data["seccion"]
    producto_marca.coleccion = self.cleaned_data["coleccion"]
    producto_marca.descuento = self.cleaned_data["descuento"]
    producto_marca.unidad_minima_descuento = self.cleaned_data["unidad_minima_descuento"]
    producto_marca.descripcion = self.cleaned_data["descripcion"]
    producto_marca.nombre = self.cleaned_data["nombre"].upper()
    pre = producto_marca.nombre[0:4]
    rabd = random.randint(0, 9999)
    producto_marca.referencia = "-" + pre + "-" + \
        "{:0>3}".format(str(len(producto_marca.nombre))) + \
        "-" + "{:0>4}".format(str(rabd))
    return producto_marca


def consultar_all():
    consulta = ProductoMarca.objects.all().order_by('seccion', 'coleccion', 'nombre')
    return consulta


def consultar_search(search):
    consulta = ProductoMarca.objects.filter(
        Q(costo__icontains=search) |
        Q(descuento__icontains=search) |
        Q(referencia__icontains=search) |
        Q(nombre__icontains=search) |
        Q(costo__icontains=search) |
        Q(descripcion__icontains=search)
    ).order_by('seccion', 'coleccion', 'nombre')
    return consulta
