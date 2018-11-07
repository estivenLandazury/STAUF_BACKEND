from django.urls import path
from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^usuarios$', views.UsuarioList.as_view()),
    url(r'^usuario/(?P<pk>[0-9]+)$', views.UsuarioDetail.as_view()),
    
    url(r'^tipoUsuarios$', views.TipoUsuerList.as_view()),            
    url(r'^tipoUsuario/(?P<pk>[0-9]+)$', views.TipoUserDetail.as_view()),

    url(r'^rolUsuarios$', views.RolUsuerList.as_view()),            
    url(r'^rolUsuario/(?P<pk>[0-9]+)$', views.RolUserDetail.as_view()),

    url(r'^Encargados$', views.UsuarioEncargadoList.as_view()),            
    url(r'^Encargado/(?P<pk>[0-9]+)$', views.UsuarioEncargadoDetail.as_view()),

    url(r'^Cuentas$', views.CuentaList.as_view()),            
    url(r'^Cuenta/(?P<pk>[0-9]+)$', views.CuentaDetail.as_view()),

    url(r'^Tipodocumentos$', views.TipoDocumentoList.as_view()),            
    url(r'^TipoDocumento/(?P<pk>[0-9]+)$', views.TipoDocumentoDetail.as_view()),

    url(r'^UsuarioDocumentos$', views.UsuarioDocumentoList.as_view()),            
    url(r'^UsuarioDocumento/(?P<pk>[0-9]+)$', views.UsuarioDocumentoDetail.as_view()),

    url(r'^Manillas$', views.ManillaList.as_view()),            
    url(r'^Manilla/(?P<pk>[0-9]+)$', views.ManillaDetail.as_view()),

    url(r'^ManillaUsuarios$', views.ManillaUsuarioList.as_view()),            
    url(r'^ManillaUsuario/(?P<pk>[0-9]+)$', views.ManillaUsuarioDetail.as_view()),


    url(r'^Apps$', views.AppMovilList.as_view()),            
    url(r'^App/(?P<pk>[0-9]+)$', views.AppMovilDetail.as_view()),

    url(r'^UsuarioApps$', views.UsuarioAppMovilList.as_view()),            
    url(r'^UsuarioApp/(?P<pk>[0-9]+)$', views.UsuarioAppMovilDetail.as_view()),

    url(r'^ManillaApps$', views.ManillaAppList.as_view()),            
    url(r'^ManillaApp/(?P<pk>[0-9]+)$', views.ManillaAppDetail.as_view()),

    url(r'^Permisos$', views.PermisoList.as_view()),            
    url(r'^Permiso/(?P<pk>[0-9]+)$', views.PermisoDetail.as_view()),

    url(r'^PermisoUsuarios$', views.PermisoUsuarioList.as_view()),            
    url(r'^PermisoUsuario/(?P<pk>[0-9]+)$', views.PermisoUsuarioDetail.as_view()),

    url(r'^Alarmas$', views.AlarmaList.as_view()),            
    url(r'^Alarma/(?P<pk>[0-9]+)$', views.AlarmaDetail.as_view()),
    


]
