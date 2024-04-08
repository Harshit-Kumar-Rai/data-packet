from rest_framework import viewsets
from .models import IOTData
from .serializer import IOTDataSerializer

class IOTDataViewSet(viewsets.ModelViewSet):
  queryset = IOTData.objects.all()
  serializer_class = IOTDataSerializer