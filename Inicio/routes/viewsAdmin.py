from django.shortcuts import render, get_object_or_404, redirect
from ..models import *
from django.contrib import messages
from unidecode import unidecode
from django.contrib.auth.models import User


def index(request):
    return render(request, 'administrador/index.html')

# USUARIO

# INASISTENCIA
def admin_lista_inasistencia(request):
    inasistencias = Inasistencia.objects.all()
    return render(request, 'administrador/inasistencia/lista.html', {'inasistencias': inasistencias})

def admin_create_inasistencia(request):
    if request.method == 'POST':
        descripcion = request.POST['descripcion']
        imagen = request.FILES.get('imagen')
       
        
        estudiante = User.objects.first()  # Esto obtiene el primer usuario, cambia esto según tus necesidades
        
        inasistencia = Inasistencia.objects.create(estudiante=estudiante, descripcion=descripcion, imagen=imagen)
        inasistencia.save()
        
        messages.success(request, 'Creado correctamente')
        return redirect('admin_lista_inasistencia')
    else:
        return render(request, 'administrador/inasistencia/create.html')



