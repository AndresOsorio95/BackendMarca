from django.shortcuts import redirect, render, get_object_or_404
from django.urls.conf import include
from django.db.models import F, Sum, Count
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from producto_bodega_detalle_app.models import ProductoBodegaDetalle
from producto_bodega_detalle_app.forms import ProductoBodegaDetalleForm
from producto_bodega_app.models import ProductoBodega
from bodega_app.models import Bodega
from administracion_app.forms import ReporteBodegaForm
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import csv
import datetime


def admin_producto_bodega_detalle_agregar(request, uuid):
    producto_bodega = get_object_or_404(ProductoBodega, uuid=uuid)
    detalles = ProductoBodegaDetalle.objects.filter(producto_bodega=uuid)
    data = {'producto_bodega': producto_bodega,
            'detalles': detalles, 'form': ProductoBodegaDetalleForm}
    if producto_bodega.is_relacionado:
        messages.success(request, 'La mercancia ya fue inventariada.')
        return redirect(to="admin_producto_bodega_inicio")
    else:
        if request.method == 'POST':
            formulario = ProductoBodegaDetalleForm(data=request.POST)
            if formulario.is_valid():
                nuevo_registro = preparar_registro(formulario, producto_bodega)
                bodega = get_object_or_404(
                    Bodega, uuid=nuevo_registro.producto_bodega.bodega.uuid)
                if bodega.capacidad_disponible == 0:
                    messages.success(
                        request, 'La mercancia ya fue inventariada.')
                    return redirect(to="admin_producto_bodega_inicio")
                else:
                    nuevo_registro.save()
                    messages.success(
                        request, 'Articulo registrado en el inventario correctamente.')
            else:
                messages.success(request, 'La mercancia ya fue inventariada.')
                return redirect(to="admin_producto_bodega_inicio")
    producto_bodega = get_object_or_404(ProductoBodega, uuid=uuid)
    data["producto_bodega"] = producto_bodega
    return render(request, 'administracion_app/producto_bodega/detalle/agregar.html', data)


def admin_producto_bodega_detalle_listar_talla(request, uuid):
    producto_bodega = get_object_or_404(ProductoBodega, uuid=uuid)
    detalles = ProductoBodegaDetalle.objects.filter(producto_bodega=uuid)
    detalles_talla = ProductoBodegaDetalle.objects.filter(
        producto_bodega=uuid).values('talla').annotate(cantidad=Count('talla'))
    data = {'producto_bodega': producto_bodega,
            'detalles': detalles, 'detalles_talla': detalles_talla}
    return render(request, 'administracion_app/producto_bodega/detalle/listar_talla.html', data)


def admin_producto_bodega_detalle_listar_color(request, uuid):
    producto_bodega = get_object_or_404(ProductoBodega, uuid=uuid)
    detalles = ProductoBodegaDetalle.objects.filter(producto_bodega=uuid)
    detalles_color = ProductoBodegaDetalle.objects.filter(
        producto_bodega=uuid).values('color').annotate(cantidad=Count('color'))
    data = {'producto_bodega': producto_bodega,
            'detalles': detalles, 'detalles_color': detalles_color}
    return render(request, 'administracion_app/producto_bodega/detalle/listar_color.html', data)


def admin_producto_bodega_detalle_listar_estado(request, uuid):
    producto_bodega = get_object_or_404(ProductoBodega, uuid=uuid)
    detalles = ProductoBodegaDetalle.objects.filter(producto_bodega=uuid)
    detalles_estado = ProductoBodegaDetalle.objects.filter(
        producto_bodega=uuid).values('estado').annotate(cantidad=Count('estado'))
    data = {'producto_bodega': producto_bodega,
            'detalles': detalles, 'detalles_estado': detalles_estado}
    return render(request, 'administracion_app/producto_bodega/detalle/listar_estado.html', data)


def consulta_reporte():
    detalles = ProductoBodegaDetalle.objects.values(
        'created_at', 'producto_bodega', 'talla', 'color', 'estado', 'informacion'
    ).annotate(
        pb_referencia=F('producto_bodega__referencia'),
        pb_nombre=F('producto_bodega__nombre'),
        pb_costo=F('producto_bodega__costo'),
        pb_costo_u=F('producto_bodega__costo_unitario'),
        pb_proveedor=F('producto_bodega__proveedor__nombre'),
        pb_bodega=F('producto_bodega__bodega__nombre'),
        pb_cantidad=F('producto_bodega__cantidad_entra'),
        pb_disponible=F('producto_bodega__cantidad_disponible'),
        pb_stop=F('producto_bodega__cantidad_minima'),
        pb_f_ingreso=F('producto_bodega__created_at'),
        pb_descripcion=F('producto_bodega__descripcion'),
    ).order_by(
        'producto_bodega', 'talla', 'color', 'estado'
    )
    return detalles


def preparar_registro(self, producto_bodega):
    producto_bodega_detalle = ProductoBodegaDetalle()
    producto_bodega_detalle.producto_bodega = producto_bodega
    producto_bodega_detalle.talla = self.cleaned_data["talla"]
    producto_bodega_detalle.color = self.cleaned_data["color"]
    producto_bodega_detalle.estado = self.cleaned_data["estado"]
    producto_bodega_detalle.informacion = self.cleaned_data["informacion"]
    return producto_bodega_detalle


def admin_producto_bodega_reporte(request):
    productos = ProductoBodegaDetalle.objects.all().annotate(
        pb_referencia=F('producto_bodega__referencia'),
        pb_nombre=F('producto_bodega__nombre'),
        pb_costo=F('producto_bodega__costo'),
        pb_costo_u=F('producto_bodega__costo_unitario'),
        pb_proveedor=F('producto_bodega__proveedor__nombre'),
        pb_bodega=F('producto_bodega__bodega__nombre'),
        pb_cantidad=F('producto_bodega__cantidad_entra'),
        pb_disponible=F('producto_bodega__cantidad_disponible'),
        pb_stop=F('producto_bodega__cantidad_minima'),
        pb_f_ingreso=F('producto_bodega__created_at'),
        pb_descripcion=F('producto_bodega__descripcion'),
    ).order_by(
        'producto_bodega', 'talla', 'color', 'estado'
    )
    date_range = request.GET.get("date_range")
    if date_range:
        start_date = date_range[0:10]
        end_date = date_range[13:23]
        print(start_date, "--", end_date)
        if len(start_date) and len(end_date):
            print('ok')
            productos = productos.filter(
                created_at__range=[start_date, end_date])
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment: filename=Expenses' + \
                str(datetime.datetime.now())+'.csv'
            writer = csv.writer(response)
            writer.writerow([
                'REFERENCIA',
                'NOMBRE PRODUCTO',
                'PROVEEDOR',
                'BODEGA',
                'COSTO',
                'COSTO UNITRIO',
                'CABTIDAD INGRESAD',
                'CANTIDAD DISPONIBLE',
                'CANTIDAD MINIMA PERMITIDA',
                'TALLA',
                'COLOR',
                'ESTADO',
                'INFORMACION',
                'DESCRIPCION',
                'FECHA INGRESO',
                'FECHA INVENTARIO',
            ])
            for p in productos:
                print(p)
            for p in productos:
                writer.writerow([
                    p.pb_referencia,
                    p.pb_nombre,
                    p.pb_proveedor,
                    p.pb_bodega,
                    p.pb_costo,
                    p.pb_costo_u,
                    p.pb_cantidad,
                    p.pb_disponible,
                    p.pb_stop,
                    p.talla,
                    p.color,
                    p.estado,
                    p.informacion,
                    p.pb_descripcion,
                    p.pb_f_ingreso,
                    p.created_at, ]
                )
            data = {
                'productos': productos,
                'form': ReporteBodegaForm(),
            }
            return response
    data = {
        'productos': productos,
        'form': ReporteBodegaForm(),
    }
    return render(request, 'administracion_app/reports/producto_bodega.html', data)


class ReportPBView(TemplateView):
    template_name = 'administracion_app/reports/producto_bodega.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReporteBodegaForm()
        try:
            action = request.POST['action']
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                print(start_date, " * ", end_date)
                productos = consulta_reporte(request)
                if len(start_date) and len(end_date):
                    productos = productos.filter(
                        created_at__range=[start_date, end_date])
                context['productos'] = productos
            else:
                context['error'] = 'Ha ocurrido un error'
        except Exception as e:
            context['error'] = str(e)
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReporteBodegaForm()
        context['productos'] = consulta_reporte()
        return context
