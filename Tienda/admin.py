import re
from django.contrib import admin
from django.utils.html import format_html
from Tienda.models import Tipos_Bicicleta, Rodado, Color, Material_Cuadro, Producto
from Tienda.models import Pedidos_Cabecera, Pedidos_linea, Forma_Pago, Estado_Pedido

# Register your models here.
#---------------------------------------------------------------------------------------------------------------#
#Tablas de BD que el superuser va a poder ABM con las opciones por defecto
admin.site.register(Tipos_Bicicleta)
admin.site.register(Rodado)
admin.site.register(Color)
admin.site.register(Material_Cuadro)

admin.site.register(Forma_Pago)
admin.site.register(Estado_Pedido)

#---------------------------------------------------------------------------------------------------------------#
#Configuraciónes
class AdminProducto(admin.ModelAdmin):
    list_display=("tipo","rodado","color","material", "descripcion", "precio", "descuento", "cantidad", "foto", "usado","publicar")
    list_filter=("tipo","rodado","color","material")
    search_fields = ("tipo","rodado","color","material","descripcion")
    ordering = ("tipo",)
    def foto(self, obj):
        return format_html ('<img src=%s width="130" heigth="100" />' % obj.imagen.url )


admin.site.register(Producto, AdminProducto)

#---------------------------------------------------------------------------------------------------------------#
class AdminPedidos(admin.ModelAdmin):
    list_display  =("pedido","cliente","fechahora","formaPago", "estadoPedido")
    list_filter   =("cliente","formaPago", "estadoPedido")
    search_fields =("cliente","formaPago", "estadoPedido")
    ordering = ("pedido",)

admin.site.register(Pedidos_Cabecera, AdminPedidos)

#---------------------------------------------------------------------------------------------------------------#
class AdminPedidosLinea(admin.ModelAdmin):
    list_display  =("pedido", "producto", "cantidad", "precioPedido")
    list_filter   =("pedido","producto", "cantidad", "precioPedido")
    search_fields = ("pedido","producto", "cantidad", "precioPedido")
    ordering      = ("pedido",)
admin.site.register(Pedidos_linea,  AdminPedidosLinea)