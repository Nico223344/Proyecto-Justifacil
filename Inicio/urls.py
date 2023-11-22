from django.urls import path
from . import views
from .routes import viewsData
from .routes import viewsAdmin


urlpatterns = [
  path('', views.index, name='index'),
  path('auth/login', views.inicio_sesion, name='login'),
  path('auth/registrar', views.registar, name='registrar'),
  path('auth/logout', views.cerrar_sesion, name='logout'),

  # pagina Usuario
  path('home/', views.home, name='home'),
  path('home/inasistencia/', views.home_inasistencia, name='home_inasistencia'),
  path('home/historial/', views.historial_inasistencias, name='historial_inasistencias'),
  
  # pagina administrador
  path('administrador/', viewsAdmin.index, name='admin_index'),
  path('administrador/inasistencia/', viewsAdmin.admin_lista_inasistencia, name='admin_lista_inasistencia'),
  path('administrador/inasistencia/create', viewsAdmin.admin_create_inasistencia, name='admin_create_inasistencia'),
  path('administrador/inasistencia/<int:id>/edit', viewsAdmin.admin_edit_inasistencia, name='admin_edit_inasistencia'),
  path('administrador/inasistencia/<int:id>/delete', viewsAdmin.admin_delete_inasistencia, name='admin_delete_inasistencia'),



  path('data', viewsData.data, name='data'),
]