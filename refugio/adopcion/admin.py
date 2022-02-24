from django.contrib import admin
from adopcion.models import Persona, Solicitud
# Register your models here.



from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Persona

class PersonaAdmin( ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display= ('nombre','apellidos','edad','telefono')

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Solicitud

class SolicitudAdmin( ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display= ('persona','numero_mascotas','razones')
    


#class MascotaInstanceAdmin(admin.ModelAdmin):
    #list_filter = ('nombre','folio')

admin.site.register(Persona,PersonaAdmin)
admin.site.register(Solicitud,SolicitudAdmin)
