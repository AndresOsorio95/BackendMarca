from bodega_app.models.bodega import Bodega
from django.shortcuts import render
from django.views.generic import TemplateView
from administracion_app.forms import ReporteBodegaForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F, Q


def admin_bodega_report(request):
    data = {
        'form': ReporteBodegaForm(),
        'bodegas': consultar_all()
    }
    return render(request, 'administracion_app/reports/bodega.html', data)

    response = HttpResponse()

def consultar_all():
    consulta = Bodega.objects.all().annotate(
        p_ocupado=(F('capacidad_maxima') - F('capacidad_disponible')
                   )*100 / F('capacidad_maxima'),
        p_disponible=(F('capacidad_disponible')*100) / F('capacidad_maxima'),
        c_ocupada=F('capacidad_maxima') - F('capacidad_disponible'),
    ).order_by('created_at')
    return consulta


class ReportBodega(TemplateView):
    template_name = 'administracion_app/reports/bodega.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de bodega'
        context['form'] = ReporteBodegaForm()
        return context
