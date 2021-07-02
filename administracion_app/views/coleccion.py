from django.shortcuts import redirect, render, get_object_or_404
from django.urls.conf import include
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import permission_required, login_required
from coleccion_app.models import Coleccion
from coleccion_app.forms import ColeccionForm


@permission_required('administracion_app.add_coleccion')
def admin_coleccion_inicio(request):
    colecciones = Coleccion.objects.all().order_by('nombre')
    search = request.GET.get("buscar")
    if search:
        colecciones = consultar_search(search)
    data = {'colecciones': colecciones}
    return render(request, 'administracion_app/coleccion/inicio.html', data)


@permission_required('administracion_app.add_coleccion')
def admin_coleccion_agregar(request):
    colecciones = consultar_all()
    data = {'colecciones': colecciones, 'form': ColeccionForm}
    if request.method == 'POST':
        formulario = ColeccionForm(data=request.POST)
        if formulario.is_valid():
            data = agregar(formulario)
            data.save()
            messages.success(request, "Coleccione agregado correctamente.")
            return redirect(to="admin_coleccion_inicio")
        else:
            data["form"] = formulario
    return render(request, 'administracion_app/coleccion/agregar.html', data)


@permission_required('administracion_app.change_coleccion')
def admin_coleccion_modificar(request, uuid):
    coleccion = get_object_or_404(Coleccion, uuid=uuid)
    data = {'coleccion': coleccion,
            'form': ColeccionForm(instance=coleccion)}
    if request.method == 'POST':
        formulario = ColeccionForm(data=request.POST, instance=coleccion)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Coleccion modificado correctamente.")
            return redirect(to="admin_coleccion_inicio")
        else:
            data["form"] = formulario
    return render(request, 'administracion_app/coleccion/modificar.html', data)


@permission_required('administracion_app.delete_coleccion')
def admin_coleccion_eliminar(request, uuid):
    coleccion = get_object_or_404(Coleccion, uuid=uuid)
    coleccion.delete()
    messages.success(request, "Coleccion eliminado correctamente.")
    return redirect(to="admin_coleccion_inicio")


def agregar(self):
    coleccion = Coleccion()
    coleccion.nombre = self.cleaned_data["nombre"].upper()
    coleccion.icono = self.cleaned_data["icono"]
    coleccion.descripcion = self.cleaned_data["descripcion"]
    print(coleccion)
    return coleccion


def consultar_all():
    consulta = Coleccion.objects.all().order_by('nombre')
    return consulta


def consultar_search(search):
    consulta = Coleccion.objects.filter(
        Q(nombre__icontains=search) | Q(descripcion__icontains=search)
    ).order_by('nombre')
    return consulta
