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
        fecha = request.POST.get('fecha')
        estado = request.POST.get('estado')
       
        
        estudiante = User.objects.first()  # Esto obtiene el primer usuario, cambia esto según tus necesidades
        
        inasistencia = Inasistencia.objects.create(estudiante=estudiante, descripcion=descripcion, imagen=imagen,fecha=fecha,estado=estado)
        inasistencia.save()
        
        messages.success(request, 'Creado correctamente')
        return redirect('admin_lista_inasistencia')
    else:
        return render(request, 'administrador/inasistencia/create.html')
    
def admin_edit_inasistencia(request, id):
    inasistencia = Inasistencia.objects.get(id=id)
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        estado = request.POST.get('estado')
        
        inasistencia.descripcion = descripcion
        inasistencia.estado = estado
        inasistencia.save()
    
    context = {'inasistencia': inasistencia}
    messages.success(request, 'Editado correctamente')
    return render(request, 'administrador/inasistencia/edit.html', context)

def admin_delete_inasistencia(request, id):
    inasistencia = Inasistencia.objects.get(id=id)
    inasistencia.delete()
    inasistencias = Inasistencia.objects.all()
    messages.warning(request, 'Eliminado correctamente')
    return render(request, 'administrador/inasistencia/lista.html', {"inasistencias":inasistencias})



