from rest_framework import serializers

from shopping_list.models import Shoppingitem

class ShoppingitemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shoppingitem
        fields = ['id','name','purchased']
        read_only_fields =('id',)