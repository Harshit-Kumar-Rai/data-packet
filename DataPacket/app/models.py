from django.db import models

class IOTData(models.Model):
  DataPacket = models.CharField(max_length=256, verbose_name='DataPacket')
  DataDetails = models.CharField(max_length=256, verbose_name='DataDetails')
  
  def __str__(self):
    return self.DataDetails

  class Meta:
    db_table  = 'iotdata'
    
    