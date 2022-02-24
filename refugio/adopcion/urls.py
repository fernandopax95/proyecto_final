from django.conf.urls import url
from django.contrib.auth.views import login_required
from usuario.views import inicio

from adopcion.views import index_adopcion, SolicitudList, SolicitudCreate, SolicitudUpdate, \
	SolicitudDelete, ListSolicitudesPDF

urlpatterns = [
    url(r'^$', inicio, name='inicio'),
    url(r'^index$', index_adopcion,name='index_adopcion'),
    url(r'^solicitud/listar$', SolicitudList.as_view(), name='solicitud_listar'),
    url(r'^solicitud/nueva$', SolicitudCreate.as_view(), name='solicitud_crear'),
    url(r'^solicitud/editar/(?P<pk>\d+)$', SolicitudUpdate.as_view(), name='solicitud_editar'),
    url(r'^solicitud/eliminar/(?P<pk>\d+)$', SolicitudDelete.as_view(), name='solicitud_eliminar'),
    url(r'^solicitud/listar-pdf/', ListSolicitudesPDF.as_view(), name = "solicitud_listar_pdf"),

]