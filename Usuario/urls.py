from django.urls import path
from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^usuario$', views.UsuarioList.as_view()),
    url(r'^usuarios/(?P<pk>[0-9]+)$', views.UsuarioDetail.as_view()),

]
