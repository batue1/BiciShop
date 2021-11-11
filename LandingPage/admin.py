from django.contrib import admin
from django.utils.html import format_html
from LandingPage.models import Empresa, Pagina, Secciones

# Register your models here.
admin.site.register(Empresa)
admin.site.register(Pagina)

class AdminSecciones(admin.ModelAdmin):
    def foto(self, obj):
        return format_html ('<img src=%s width="130" heigth="100" />' % obj.imagen.url )


admin.site.register(Secciones, AdminSecciones)
