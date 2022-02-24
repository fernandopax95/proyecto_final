from django.contrib import admin
from .models import Mascota, Vacuna
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Mascota

class MascotaAdmin( ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display= ('nombre','folio')

#class MascotaInstanceAdmin(admin.ModelAdmin):
    #list_filter = ('nombre','folio')

admin.site.register(Mascota,MascotaAdmin)
admin.site.register(Vacuna)

