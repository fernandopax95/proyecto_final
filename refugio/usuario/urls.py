from django.conf.urls import url,include
from .views import RegistroCaras, ValidarCara,   inicio, acceder, fail,salir,VistaRegistro #crearUsuario,


urlpatterns = [
   url(r'^$', inicio, name='inicio'),
   url(r'^caras/', RegistroCaras, name='caras'),
   url(r'^registrar/', VistaRegistro.as_view(), name='registrar_usuario'),
   url(r'^validar_rostro/', ValidarCara, name='validar_rostro'), 
   url(r'^acceder/', acceder, name='acceder'),
   url(r'^salir/', salir, name='salir'),
   url(r'^fail/', fail, name='fail'),
   

]