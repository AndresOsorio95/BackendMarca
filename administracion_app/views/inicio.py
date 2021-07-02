from django.shortcuts import render

from django.contrib.auth.decorators import permission_required, login_required


@permission_required('tienda_app.add_bodega')
def admin_inicio(request):
    return render(request, 'administracion_app/inicio/base.html')
