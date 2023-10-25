from django.urls import path
from . import views
from . import viewsLogin
# api/v1/
urlpatterns = [
    path('auth/', viewsLogin.login, name='api_auth'),
    
    path('inasistencia/', views.lista_inasistencia, name='lista_inasistencia'),
    path('inasistencia/<id>', views.vista_inasistencia, name='vista_inasistencia'),
]