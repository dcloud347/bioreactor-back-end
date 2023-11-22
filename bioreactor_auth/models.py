from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class DeviceAuthenticationToken(models.Model):
    name = models.CharField(max_length=100, verbose_name='Device Name', unique=True, primary_key=True)
    token = models.CharField(max_length=100, verbose_name='Token', unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_devices',
                                   verbose_name='creator')

    class Meta:
        verbose_name = verbose_name_plural = 'Device token for bioreactor'

    def __str__(self):
        return f'{self.name}'
