from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=settings.ROLES)

    def __str__(self):
        return self.user.username + ' - ' + self.role
    

class Inasistencia(models.Model):
    estudiante =  models.ForeignKey('auth.User', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='media/inasistencias', null=True)
    fecha = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.descripcion
