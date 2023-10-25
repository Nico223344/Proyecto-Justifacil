from django.shortcuts import redirect
from ..models import  *
from django.contrib.auth.models import User

# RANDOM DATA
from faker import Faker
from django.contrib.auth import get_user_model
from django.conf import settings
import random
from unidecode import unidecode

# Reemplazar espacios con guiones bajos, convertir a minúsculas y quitar acentos


def convertir_a_formato_variable(cadena):
    return unidecode(cadena.lower().replace(' ', '_'))

# guardar datos


def data(request):
    fake = Faker()
    roles = [role[0] for role in settings.ROLES]

    # Limpiar datos existentes si es necesario
    User.objects.all().delete()
    UserProfile.objects.all().delete()
    Inasistencia.objects.all().delete()

    # crea 2 usuarios
    user = get_user_model().objects.create_user(
        username="admin", email="admin@gmail.com", password="12345")
    UserProfile.objects.create(user=user, role='admin')

    user = get_user_model().objects.create_user(username="cliente",
                                                email="cliente@gmail.com", password="12345")
    UserProfile.objects.create(user=user, role='cliente')

    # Crea usuarios de ejemplo con roles
    for _ in range(10):
        username = fake.user_name()
        email = fake.email()
        password = '123456'
        role = random.choice(roles)

        user = get_user_model().objects.create_user(
            username=username, email=email, password=password)
        UserProfile.objects.create(user=user, role=role)



    array_inasistencias = [
      ['Inasistencia 1',  1, 'Descripción de la inasistencia 1'],
      ['Inasistencia 2',  1, 'Descripción de la inasistencia 2'],
      ['Inasistencia 3',  2, 'Descripción de la inasistencia 3'],
      # Agrega más inasistencias aquí
    ]

    for _ in range(20):
        inasistencia_data = array_inasistencias[random.randint(0, len(array_inasistencias) - 1)]
        descripcion_inasistencia = inasistencia_data[3]
        codigo_inasistencia = fake.unique.random_number()

        Inasistencia.objects.create(
            codigo=codigo_inasistencia,
            descripcion=descripcion_inasistencia,
        )
