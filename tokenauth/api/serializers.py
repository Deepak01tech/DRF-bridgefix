from rest_framework import serializers
from .models import fresh

class freshserializers(serializers.ModelSerializer):
    class Meta:
        model=fresh
        fields='__all__'