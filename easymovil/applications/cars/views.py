from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView
    
    )

from rest_framework.authentication import (
    TokenAuthentication
)
from rest_framework.permissions import (IsAuthenticated,IsAdminUser)

#Modelo car
from . models import Car
#Serializador para modelo car
from . serializers import CarSerializer


class CarCreateApiView(CreateAPIView):
    """Vista para crear objeto car (C)"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdminUser]
    
    serializer_class = CarSerializer

    
class CarListApiView(ListAPIView):
    """Vista para Leer lista de objetos car (R)"""
    serializer_class = CarSerializer
    #Desencriptar token
    authentication_classes = (TokenAuthentication,)
    #tipo de permiso que pose el usuario (usuario razo)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print('XXXXXXXXXXXXXXXX')
        print(self.request.user)
        return Car.objects.all()


class CarUpdateView(RetrieveUpdateAPIView):
    """Vista para actualizar objeto car (U)"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdminUser]
    
    serializer_class = CarSerializer
    queryset= Car.objects.all()
    
    
class CarDeleteView(DestroyAPIView):
    """Vista para eliminar objeto car (D)"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdminUser]
        
    serializer_class = CarSerializer
    queryset= Car.objects.all()

    
    
