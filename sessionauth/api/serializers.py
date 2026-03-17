from rest_framework import serializers

from . models import Mega

class Megaserializer(serializers.ModelSerializer):
    class Meta:
        model=Mega
        fields = '__all__'