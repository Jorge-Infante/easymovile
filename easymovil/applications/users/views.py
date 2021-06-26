#dj rest
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Firebase
from firebase_admin import auth
#django
from django.shortcuts import render
from django.views.generic import TemplateView

#Serializador
from . serializers import LoginSocialSerializer
#Modelo usuario
from . models import User


class LoginUser(TemplateView):
    """Vista para llamada al api firebase para generar el token"""
    template_name = "users/login.html"
    

class GoogleLoginView(APIView):
    """Vista para procesar token"""
    serializer_class = LoginSocialSerializer
    
    #Creando token propio
    
    def post(self, request):
        #serializar data 
        serializer = self.serializer_class(data=request.data)
        #verificamos que contenga un valor valido para el serializer
        serializer.is_valid(raise_exception=True)
        #Recupero valor
        id_token = serializer.data.get('token_id')
        #desencriptar serializer
        decoded_token = auth.verify_id_token(id_token)
        
        #Usar los valores del token ya decodificado
        
        email = decoded_token['email']
        name = decoded_token['name']
        avatar = decoded_token['picture']
        verified = decoded_token['email_verified']
        
        usuario, created = User.objects.get_or_create(
            email=email,
            defaults={
                'full_name': name,
                'email': email,
                'is_active': True
            }
        )
        
        #obtener el get or create
        #T rest
        if created:
            token = Token.objects.create(user=usuario)
        else:
            token= Token.objects.get(user=usuario)
        
        userGet = {
            'id' : usuario.pk,
            'email' : usuario.email,
            'full_name' : usuario.full_name,
            'genero' : usuario.genero,
            'date_birth' : usuario.date_birth,
            'city' : usuario.city
        }
        return Response(
            {
                'token' : token.key,
                'user' : userGet,
            }
        )
