from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import role_required
from django.contrib.auth.models import User
from django.contrib import messages

## REQUESTS
import requests
from django.http import JsonResponse

# inicio de todo
def index(request):
    return render(request, 'index.html')

# AUTH
def inicio_sesion (request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        clave = request.POST.get('pass')
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            profile = UserProfile.objects.get(user=user)
            request.session['perfil'] = profile.role

            login(request, user)
            return redirect('home')
        else:
            context = {
                'error' : 'Error intente nuevamente.'
            }
            return render(request, 'auth/index.html', context)

    return render(request, 'auth/index.html')

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('index')


def registar(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        first_name = request.POST.get('nombre')
        last_name = request.POST.get('apellido')
        email = request.POST.get('correo')
        password = request.POST.get('pass')

        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
    
        role = request.POST.get('tipo')
        UserProfile.objects.create(user=user, role=role)

        messages.success(request, 'Creado correctamente')

        return redirect('login')

    return render(request, 'auth/create.html')

# SISTEMA
@login_required
def home(request):
    perfil = request.session.get('perfil')
    inasistencias = Inasistencia.objects.all()


    context = {
        'perfil' : perfil,
        'inasistencias' : inasistencias,
    }

    return render(request, 'home.html', context)

def home_inasistencia(request):
    if request.method == 'POST':
        descripcion = request.POST['descripcion']
        imagen = request.FILES.get('imagen')
        fecha = request.POST.get('fecha')
        
        
            
        estudiante = request.user
            
        inasistencia = Inasistencia.objects.create(estudiante=estudiante, descripcion=descripcion, imagen=imagen, fecha=fecha)
        inasistencia.save()
            
        messages.success(request, 'Creado correctamente')
        return redirect('home_inasistencia')
    else:
        return render(request, 'inasistencia.html')

#Historial de inasistencia 
def historial_inasistencias(request):
    inasistencias = Inasistencia.objects.filter(estudiante=request.user)
    return render(request, 'historial.html', {'inasistencias': inasistencias})

