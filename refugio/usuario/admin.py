from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

#from django.apps import apps
#from simple_history.admin import SimpleHistoryAdmin
from django.contrib.auth.models import User
# Register your models here.
#admin.site.register(User)

#class UsuarioAdmin(SimpleHistoryAdmin):
    #list_display=('nombre')

#admin.site.register(User, UsuarioAdmin)

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = User

class UserAdmin (ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['name', 'email', 'username']
    resources_class = CategoriaResource

#admin.site.register( UserAdmin)