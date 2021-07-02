from administracion_app.views.producto_bodega import admin_producto_bodega_agregar, admin_producto_bodega_inicio
from administracion_app.views import *
from django.urls import path

urlpatterns = [
    path('marca/inicio/', admin_inicio, name="admin_inicio"),
    path('registro/', registro, name="registro"),
    # Bodega
    path('marca/bodegas/', admin_bodega_inicio, name="admin_bodega_inicio"),
    path('marca/bodegas/agregar/', admin_bodega_agregar,
         name="admin_bodega_agregar"),
    path('marca/bodegas/modificar/<uuid>/',
         admin_bodega_modificar, name="admin_bodega_modificar"),
    path('marca/bodegas/eliminar/<uuid>/',
         admin_bodega_eliminar, name="admin_bodega_eliminar"),
    path('marca/bodegas/report/', generar_csv, name='reporte_bodega'),
    # Proveedor
    path('marca/proveedores/', admin_proveedor_inicio,
         name="admin_proveedor_inicio"),
    path('marca/proveedores/agregar/', admin_proveedor_agregar,
         name="admin_proveedor_agregar"),
    path('marca/proveedores/modificar/<uuid>/',
         admin_proveedor_modificar, name="admin_proveedor_modificar"),
    path('marca/proveedores/eliminar/<uuid>/',
         admin_proveedor_eliminar, name="admin_proveedor_eliminar"),
    # Seccion
    path('marca/secciones/', admin_seccion_inicio,
         name="admin_seccion_inicio"),
    path('marca/secciones/agregar/', admin_seccion_agregar,
         name="admin_seccion_agregar"),
    path('marca/secciones/modificar/<uuid>/',
         admin_seccion_modificar, name="admin_seccion_modificar"),
    path('marca/secciones/eliminar/<uuid>/',
         admin_seccion_eliminar, name="admin_seccion_eliminar"),
    # Coleccion
    path('marca/colecciones/', admin_coleccion_inicio,
         name="admin_coleccion_inicio"),
    path('marca/colecciones/agregar/', admin_coleccion_agregar,
         name="admin_coleccion_agregar"),
    path('marca/colecciones/modificar/<uuid>/',
         admin_coleccion_modificar, name="admin_coleccion_modificar"),
    path('marca/colecciones/eliminar/<uuid>/',
         admin_coleccion_eliminar, name="admin_coleccion_eliminar"),
    # Producto bodega
    path('marca/productos/b/', admin_producto_bodega_inicio,
         name="admin_producto_bodega_inicio"),
    path('marca/productos/b/agregar/', admin_producto_bodega_agregar,
         name="admin_producto_bodega_agregar"),
    path('marca/productos/b/reports/', admin_producto_bodega_reporte,
         name="admin_producto_bodega_reporte"),
     path('marca/productos/b/report/', ReportPBView.as_view(),name='report-pb'),
    # Producto bodega detalle
    path('marca/productos/b/d/agregar/<uuid>/',
         admin_producto_bodega_detalle_agregar, name="admin_producto_bodega_detalle_agregar"),
    path('marca/productos/b/d/t/<uuid>/',
         admin_producto_bodega_detalle_listar_talla, name="admin_producto_bodega_detalle_listar_talla"),
    path('marca/productos/b/d/c/<uuid>/',
         admin_producto_bodega_detalle_listar_color, name="admin_producto_bodega_detalle_listar_color"),
    path('marca/productos/b/d/e/<uuid>/',
         admin_producto_bodega_detalle_listar_estado, name="admin_producto_bodega_detalle_listar_estado"),
    # Producto MARCA
    path('marca/productos/m/', admin_producto_marca_inicio,
         name="admin_producto_marca_inicio"),
    path('marca/productos/m/crear/', admin_producto_marca_agregar,
         name="admin_producto_marca_agregar"),
    # Producto Bodega MARCA
    path('marca/productos/m/d/agregar/<uuid>/', admin_producto_bodega_marca_agregar,
         name="admin_producto_bodega_marca_agregar"),
    path('marca/productos/m/d/agregar/<uuid_bodega>/<uuid_marca>',
         admin_producto_bodega_marca_agregar_detalle, name="admin_producto_bodega_marca_agregar_detalle"),
    path('marca/productos/m/e/d/<producto_bodeg_uuid>/<producto_marca_uuid>/', admin_producto_bodega_marca_eliminar_detalle_,
         name="admin_producto_bodega_marca_eliminar_detalle_"),
    # Imagen Producto Marca
    path('marca/productos/m/i/<uuid>/', admin_producto_bodega_marca_agregar_imagen,
         name="admin_producto_bodega_marca_agregar_imagen"),
    path('marca/productos/m/d/<uuid>/', admin_producto_bodega_marca_listar_imagen,
         name="admin_producto_bodega_marca_listar_imagen"),
    path('marca/productos/m/e/<uuid>/', admin_producto_bodega_marca_eliminar,
         name="admin_producto_bodega_marca_eliminar"),
    path('marca/productos/m/e/a/<producto_bodeg_uuid>/<producto_marca_uuid>/', admin_producto_bodega_marca_eliminar_detalle,
         name="admin_producto_bodega_marca_eliminar_detalle"),

]
