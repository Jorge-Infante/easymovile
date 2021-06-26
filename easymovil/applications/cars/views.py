from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView
    
    )
#Modelo car
from . models import Car
#Serializador para modelo car
from . serializers import CarSerializer


class CarCreateApiView(CreateAPIView):
    """Vista para crear objeto car (C)"""
    serializer_class = CarSerializer

    
class CarListApiView(ListAPIView):
    """Vista para Leer lista de objetos car (R)"""
    serializer_class = CarSerializer
    
    def get_queryset(self):
        return Car.objects.all()


class CarUpdateView(RetrieveUpdateAPIView):
    """Vista para actualizar objeto car (U)"""
    serializer_class = CarSerializer
    queryset= Car.objects.all()
    
    
class CarDeleteView(DestroyAPIView):
    """Vista para eliminar objeto car (D)"""
    serializer_class = CarSerializer
    queryset= Car.objects.all()

    
    
