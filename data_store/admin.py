from django.contrib import admin
from .models import Record, DesiredValues

# Register your models here.

admin.site.site_header = "Group 17's Bioreactor Management"
admin.site.index_title = 'Bioreactor'


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'value', 'time']


@admin.register(DesiredValues)
class DesiredValuesAdmin(admin.ModelAdmin):
    list_display = ['name', 'desired_value']
