from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class usuario(models.Model):
    """Clase que Extiende al Usuario de Django."""
    user=models.OneToOneField(User)
    telefono=models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.user.username