from django.db import models
from model_utils.models import TimeStampedModel


class Car(TimeStampedModel):
    """ Modelo para registrar carro"""
    
    model=models.CharField(
        'Model', 
        max_length=50,
    )
    color=models.CharField(
        'Color', 
        max_length=50,
    )
    
    date = models.DateField()
    
    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
    
    def __str__(self):
        return 'ID : '+str(self.id) +' Model: '+ self.model +' Color: '+ self.color +' Fecha: '+str(self.date)
