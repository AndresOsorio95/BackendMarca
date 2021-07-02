from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import permission_required, login_required
from proveedor_app.models import Proveedor
from proveedor_app.forms import ProveedorForm


@permission_required('administracion_app.add_proveedor')
def admin_proveedor_inicio(request):
    proveedores = consultar_all()
    search = request.GET.get("buscar")
    if search:
        proveedores = consultar_search(search)
    data = {'proveedores': proveedores}
    return render(request, 'administracion_app/proveedor/inicio.html', data)


@permission_required('administracion_app.add_proveedor')
def admin_proveedor_agregar(request):
    proveedores = consultar_all()
    data = {'proveedores': proveedores, 'form': ProveedorForm}
    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST)
        if formulario.is_valid():
            data = agregar(formulario)
            data.save()
            messages.success(request, "Proveedore agregado correctamente.")
            return redirect(to="admin_proveedor_inicio")
        else:
            data["form"] = formulario
    return render(request, 'administracion_app/proveedor/agregar.html', data)


@permission_required('administracion_app.change_proveedor')
def admin_proveedor_modificar(request, uuid):
    proveedor = get_object_or_404(Proveedor, uuid=uuid)
    data = {'proveedor': proveedor,
            'form': ProveedorForm(instance=proveedor)}
    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, instance=proveedor)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Proveedor modificado correctamente.")
            return redirect(to="admin_proveedor_inicio")
        else:
            data["form"] = formulario
    return render(request, 'administracion_app/proveedor/modificar.html', data)


@permission_required('administracion_app.delete_proveedor')
def admin_proveedor_eliminar(request, uuid):
    proveedor = get_object_or_404(Proveedor, uuid=uuid)
    proveedor.delete()
    messages.success(request, "Proveedor eliminado correctamente.")
    return redirect(to="admin_proveedor_inicio")


def agregar(self):
    proveedor = Proveedor()
    proveedor.tipo_identificacion = self.cleaned_data["tipo_identificacion"]
    proveedor.identificacion = self.cleaned_data["identificacion"]
    proveedor.nombre = self.cleaned_data["nombre"].upper()
    proveedor.direccion = self.cleaned_data["direccion"].upper()
    proveedor.numero_telefonico = self.cleaned_data["numero_telefonico"]
    proveedor.correo_electronico = self.cleaned_data["correo_electronico"]
    proveedor.descripcion = self.cleaned_data["descripcion"]
    print(proveedor)
    return proveedor


def consultar_all():
    consulta = Proveedor.objects.all().order_by('nombre')
    return consulta


def consultar_search(search):
    consulta = Proveedor.objects.filter(
        Q(nombre__icontains=search) |
        Q(descripcion__icontains=search) |
        Q(numero_telefonico__icontains=search) |
        Q(correo_electronico__icontains=search) |
        Q(descripcion__icontains=search) |
        Q(identificacion__icontains=search)
    ).order_by('nombre')
    return consulta
