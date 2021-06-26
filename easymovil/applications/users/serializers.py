from rest_framework import serializers

class LoginSocialSerializer(serializers.Serializer):
    """Serializador para capturar el toquen"""
    token_id = serializers.CharField(required=True)
    
