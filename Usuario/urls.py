from django.urls import path
from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^usuarios$', views.UsuarioList.as_view()),
    url(r'^usuario/(?P<numeroDocumento>[\w-]+)$', views.UsuarioDetail.as_view()),
    url(r'^usuarioId/(?P<pk>[0-9]+)$', views.UsuarioDetailId.as_view()),

    url(r'^getUsu', views.UsuarioLista.as_view()),
    url(r'^usuariosSecundarios$', views.ObtenerUsuariosPorRolesSecundarios.as_view()),

    

    
    url(r'^prueba',views.ObtenerUsuarioCuenta.as_view()),
    url(r'^UsuarioCuenta/(?P<user>[\w-]+)$',views.UsuarioDetailCuenta.as_view()),



    
    url(r'^tipoUsuarios$', views.TipoUsuerList.as_view()),            
    url(r'^tipoUsuario/(?P<pk>[0-9]+)$', views.TipoUserDetail.as_view()),
    url(r'^filterTipoUsuario$', views.FilterTipoUsuarioList.as_view()),            


    url(r'^rolUsuarios$', views.RolUsuerList.as_view()),            
    url(r'^rolIdUsuario', views.obtenerRolPorIdUsuario.as_view()),            
    url(r'^rolUsuario/(?P<usuario>[\w-]+)$', views.RolUserDetail.as_view()),


    url(r'^Encargados$', views.UsuarioEncargadoList.as_view()),       
    url(r'^EncargadoActual', views.FiltrarncargadoyFechaActual.as_view()),            
    url(r'^Encargado/(?P<pk>[0-9]+)$', views.UsuarioEncargadoDetail.as_view()),
    url(r'^UsuarioEncargado/(?P<idEncargado>[\w-]+)$', views.UsuarioEncargadoIdEncargado.as_view()),

   
    url(r'^Autenticade$', views.autenticacion),
    url(r'^AddUser$',views.createUser),
    url(r'^GetUsers$',views.UserAuthList.as_view()),
    url(r'^GetCuenta',views.obtenerCuentaPorUserName.as_view()),
    url(r'^GetUser/(?P<username>[\w-]+)$',views.UserAuthDetail.as_view()),


  

    url(r'^Tipodocumentos$', views.TipoDocumentoList.as_view()),            
    url(r'^TipoDocumento/(?P<pk>[0-9]+)$', views.TipoDocumentoDetail.as_view()),

    url(r'^UsuarioDocumentos$', views.UsuarioDocumentoList.as_view()),            
    url(r'^UsuarioDocumento/(?P<usuario>[\w-]+)$', views.UsuarioDocumentoDetail.as_view()),

    url(r'^Manillas$', views.ManillaList.as_view()),            
    url(r'^Manilla/(?P<macId>[\w-]+)$', views.ManillaDetail.as_view()),
    url(r'^ManillaUsuarios$', views.ManillaUsuarioList.as_view()), 
    url(r'^ManillaUsuariosFiltro', views.FiltrarManillas.as_view()),                 
    url(r'^ManillaUsuario/(?P<pk>[0-9]+)$', views.ManillaUsuarioDetail.as_view()),


    url(r'^Apps$', views.AppMovilList.as_view()),            
    url(r'^App/(?P<pk>[0-9]+)$', views.AppMovilDetail.as_view()),
    url(r'^AppName/(?P<nombre>[\w-]+)$', views.AppMovilDetailName.as_view()),


    url(r'^UsuarioApps$', views.UsuarioAppMovilList.as_view()),  
    url(r'^UsuarioAppUsu', views.filtrarUsuaripAppIdusuario.as_view()), 
    url(r'^UsuarioAppApp/(?P<appMovil>[\w-]+)$', views.filtrarUsuarioAppIdApp.as_view()),             
    url(r'^UsuarioApp/(?P<pk>[0-9]+)$', views.UsuarioAppMovilDetail.as_view()),

    url(r'^ManillaApps$', views.ManillaAppList.as_view()), 
    url(r'^ManillaAppIdAp',  views.FiltrarManillaAppPorIdApp.as_view()),                   
    url(r'^ManillaApp/(?P<pk>[0-9]+)$', views.ManillaAppDetail.as_view()),

    url(r'^Permisos$', views.PermisoList.as_view()),            
    url(r'^Permiso/(?P<pk>[0-9]+)$', views.PermisoDetail.as_view()),
    url(r'^PermisoUsuarios$', views.PermisoUsuarioList.as_view()),            
    url(r'^PermisoUsuario/(?P<pk>[0-9]+)$', views.PermisoUsuarioDetail.as_view()),

    url(r'^Alarmas$', views.AlarmaList.as_view()), 
    url(r'^AlarmasFalse', views.AlarmasFalse.as_view()),  
    url(r'^AlarmasTrue', views.AlarmasTrue.as_view()),
    url(r'^AlarmasPorFecha', views.AlarmaPorfechayIdApp.as_view()), 
    url(r'^Alarma/(?P<pk>[0-9]+)$', views.AlarmaDetail.as_view()),
    


]
