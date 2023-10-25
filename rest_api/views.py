
from django.shortcuts import render
from .serializers import InasistenciaSerializer
from Inicio.models import *
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET', 'POST'])
# @permission_classes((IsAuthenticated,)) #para que solo los usuarios autenticados puedan acceder a esta vista
def lista_inasistencia(request):
    if request.method == 'GET':
        inasistencias = Inasistencia.objects.all()  # select * from inasistencia
        serializer = InasistenciaSerializer(inasistencias, many=True)

        for inasistencia_data in serializer.data:
            inasistencia_data['imagen'] = settings.BASE_URL + '/static' + inasistencia_data['imagen']

        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = InasistenciaSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def vista_inasistencia(request, id):
    try:
        inasistencia = Inasistencia.objects.get(id=id)
    except Inasistencia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InasistenciaSerializer(inasistencia)
        return Response(serializer.data)

    elif request.method == 'PUT' or request.method == 'PATCH':
        data = JSONParser().parse(request)
        serializer = InasistenciaSerializer(inasistencia, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        inasistencia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
