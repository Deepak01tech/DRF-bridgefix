from rest_framework.viewsets import ModelViewSet

from shopping_list.api.serializers import ShoppingitemSerializer
from shopping_list.models import Shoppingitem


class ShoppingItemViewSet(ModelViewSet):
    queryset= Shoppingitem.objects.all()
    serializer_class=ShoppingitemSerializer

