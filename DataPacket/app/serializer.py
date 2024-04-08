from rest_framework import serializers
from .models import IOTData

class IOTDataSerializer(serializers.ModelSerializer):
  class Meta:
    model = IOTData
    fields = '__all__'
    db_table  = 'iotdata'