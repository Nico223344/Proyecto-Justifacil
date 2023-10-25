from rest_framework import serializers
from Inicio.models import Inasistencia

class InasistenciaSerializer(serializers.ModelSerializer):
    class Meta:
      model = Inasistencia
      fields = '__all__'
    
