from django.shortcuts import redirect, render, get_object_or_404
from django.urls.conf import include
from django.contrib import messages
from bodega_app.models import Bodega
from bodega_app.forms import BodegaForm
from django.db.models import F, Q
from django.http import HttpResponse
import csv
import datetime

from django.contrib.auth.decorators import permission_required, login_required


@permission_required('tienda_app.add_bodega')
def admin_bodega_inicio(request):
    bodegas = consultar_all()
    search = request.GET.get("buscar")
    if search:
        bodegas = consultar_search(search)
    data = {'bodegas': bodegas}
    return render(request, 'administracion_app/bodega/inicio.html', data)


def admin_bodega_agregar(request):
    bodegas = consultar_all()
    data = {'bodegas': bodegas, 'form': BodegaForm}
    if request.method == 'POST':
        formulario = BodegaForm(data=request.POST)
        if formulario.is_valid():
            data = agregar(formulario)
            data.save()
            messages.success(request, "Bodega agregada correctamente.")
            return redirect(to="admin_bodega_inicio")
        else:
            data["form"] = formulario
    return render(request, 'administracion_app/bodega/agregar.html', data)


def admin_bodega_modificar(request, uuid):
    bodega = get_object_or_404(Bodega, uuid=uuid)
    data = {'bodega': bodega, 'form': BodegaForm(instance=bodega)}
    if request.method == 'POST':
        formulario = BodegaForm(data=request.POST, instance=bodega)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Bodega modificada correctamente.")
            return redirect(to="admin_bodega_inicio")
        else:
            data["form"] = formulario
    return render(request, 'administracion_app/bodega/modificar.html', data)


def admin_bodega_eliminar(request, uuid):
    bodega = get_object_or_404(Bodega, uuid=uuid)
    bodega.delete()
    messages.success(request, "Bodega eliminada correctamente.")
    return redirect(to="admin_bodega_inicio")


def agregar(self):
    bodega = Bodega()
    bodega.nombre_corto = self.cleaned_data["nombre_corto"].upper()
    bodega.nombre = self.cleaned_data["nombre"].upper()
    bodega.capacidad_maxima = self.cleaned_data["capacidad_maxima"]
    bodega.capacidad_disponible = self.cleaned_data["capacidad_maxima"]
    bodega.direccion = self.cleaned_data["direccion"].upper()
    bodega.numero_telefonico = self.cleaned_data["numero_telefonico"]
    bodega.correo_electronico = self.cleaned_data["correo_electronico"]
    bodega.descripcion = self.cleaned_data["descripcion"]
    print(bodega)
    return bodega


def generar_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment: filename=Expenses' + \
        str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)
    writer.writerow([
        'NOMBRE CORTO',
        'NOMBRE BODEGA',
        'CAPACIDAD MAXIMA',
        'CAPACIDAD DISPONIBLE',
        'ESPCIO OCUPADO',
        'PORC. CAPACIDAD DISPONIBLE',
        'PORC. ESPACIO USADO',
        'DIRECCION',
        'TELEFONO',
        'CORREO',
        'DESCRIPCION'
    ])
    bodegas = consultar_all()
    for bodega in bodegas:
        writer.writerow([
            bodega.nombre_corto,
            bodega.nombre,
            bodega.capacidad_maxima,
            bodega.capacidad_disponible,
            bodega.c_ocupada,
            bodega.p_disponible,
            bodega.p_ocupado,
            bodega.direccion,
            bodega.numero_telefonico,
            bodega.correo_electronico,
            bodega.descripcion
        ])
    return response


def consultar_all():
    consulta = Bodega.objects.all().annotate(
        p_ocupado=(F('capacidad_maxima') - F('capacidad_disponible')
                   )*100 / F('capacidad_maxima'),
        p_disponible=(F('capacidad_disponible')*100) / F('capacidad_maxima'),
        c_ocupada=F('capacidad_maxima') - F('capacidad_disponible'),
    ).order_by('nombre')
    return consulta


def consultar_search(search):
    consulta = Bodega.objects.filter(
        Q(nombre__icontains=search) |
        Q(nombre_corto__icontains=search) |
        Q(direccion__icontains=search) |
        Q(numero_telefonico__icontains=search) |
        Q(correo_electronico__icontains=search) |
        Q(descripcion__icontains=search)
    ).annotate(
        p_ocupado=(F('capacidad_maxima') - F('capacidad_disponible')
                   )*100 / F('capacidad_maxima'),
        p_disponible=(F('capacidad_disponible')*100) / F('capacidad_maxima'),
        c_ocupada=F('capacidad_maxima') - F('capacidad_disponible'),
    ).order_by('nombre')
    return consulta
