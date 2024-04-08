from django.contrib import admin

from .models import IOTData


class IOTAdmin(admin.ModelAdmin):
  list_display = ['DataPacket', 'DataDetails']

admin.site.register(IOTData, IOTAdmin)