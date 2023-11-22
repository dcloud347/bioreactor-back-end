from django.contrib import admin
from .models import DeviceAuthenticationToken


# Register your models here.

@admin.register(DeviceAuthenticationToken)
class DeviceAuthenticationTokenAdmin(admin.ModelAdmin):
    list_display = ['name', 'token']
