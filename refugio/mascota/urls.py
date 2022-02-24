
from django.conf.urls import url,include
from .views import  mascota_delete, mascota_crear, MascotaList, mascota_edit, MascotaListImagenes, ListMascotasPDF, VacunaCreate,VacunaList, VacunaDelete, vacuna_edit, ListVacunaPDF
from usuario.views import inicio


urlpatterns = [
    url(r'^$', inicio, name='inicio'),
    url(r'^nuevo/', mascota_crear, name = "mascota_crear"),
    url(r'^listar/', MascotaList.as_view(), name = "mascota_listar"),
    url(r'^listarmascota-pdf/', ListMascotasPDF.as_view(), name = "mascota_listar_pdf"),
    url(r'^listarimagen/', MascotaListImagenes.as_view(), name = "mascota_listar_imagenes"),
    url(r'^editar/(?P<folio_mascota>\d+)/', mascota_edit, name = "mascota_editar"),
    url(r'^eliminar/(?P<folio_mascota>\d+)/', mascota_delete, name = "mascota_eliminar"),
    url(r'^nuevo-vacuna/', VacunaCreate.as_view(), name = "vacuna_crear"),
    url(r'^listarvacuna/', VacunaList.as_view(), name = "vacuna_listar"),
    url(r'^editar-vacuna/(?P<id_vacuna>\d+)/', vacuna_edit, name = "vacuna_editar"),
    url(r'^vacuna-eliminar/(?P<pk>\d+)$', VacunaDelete.as_view(), name='vacuna_eliminar'),
    url(r'^listarvacuna-pdf/', ListVacunaPDF.as_view(), name = "vacuna_listar_pdf"),


    #url(r'^export/', export_pdf, name = "export-pdf"),
]
