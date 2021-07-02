from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import permission_required, login_required
from seccion_app.models import Seccion
from seccion_app.forms import SeccionForm


@permission_required('administracion_app.add_seccion')
def admin_seccion_inicio(request):
    secciones = consultar_all()
    search = request.GET.get("buscar")
    if search:
        secciones = consultar_search(search)
    data = {'secciones': secciones}
    return render(request, 'administracion_app/seccion/inicio.html', data)


@permission_required('administracion_app.add_seccion')
def admin_seccion_agregar(request):
    secciones = consultar_all()
    data = {'secciones': secciones, 'form': SeccionForm}
    if request.method == 'POST':
        formulario = SeccionForm(data=request.POST)
        if formulario.is_valid():
            data = agregar(formulario)
            data.save()
            messages.success(request, "Seccione agregado correctamente.")
            return redirect(to="admin_seccion_inicio")
        else:
            data["form"] = formulario
    return render(request, 'administracion_app/seccion/agregar.html', data)


@permission_required('administracion_app.change_seccion')
def admin_seccion_modificar(request, uuid):
    seccion = get_object_or_404(Seccion, uuid=uuid)
    data = {'seccion': seccion, 'form': SeccionForm(instance=seccion)}
    if request.method == 'POST':
        formulario = SeccionForm(data=request.POST, instance=seccion)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Seccion modificado correctamente.")
            return redirect(to="admin_seccion_inicio")
        else:
            data["form"] = formulario
    return render(request, 'administracion_app/seccion/modificar.html', data)


@permission_required('administracion_app.delete_seccion')
def admin_seccion_eliminar(request, uuid):
    seccion = get_object_or_404(Seccion, uuid=uuid)
    seccion.delete()
    messages.success(request, "Seccion eliminado correctamente.")
    return redirect(to="admin_seccion_inicio")


def agregar(self):
    seccion = Seccion()
    seccion.nombre = self.cleaned_data["nombre"].upper()
    seccion.icono = self.cleaned_data["icono"]
    seccion.descripcion = self.cleaned_data["descripcion"]
    print(seccion)
    return seccion


def consultar_all():
    consulta = Seccion.objects.all().order_by('nombre')
    return consulta


def consultar_search(search):
    consulta = Seccion.objects.filter(
        Q(nombre__icontains=search) | Q(descripcion__icontains=search)
    ).order_by('nombre')
    return consulta
