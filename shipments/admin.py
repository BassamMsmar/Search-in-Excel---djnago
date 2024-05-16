from django.contrib import admin

from .models import Shipment, ExcelFile

admin.site.register(Shipment)
admin.site.register(ExcelFile)

# Register your models here.
