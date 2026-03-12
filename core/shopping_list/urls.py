from django.urls import path,include
from rest_framework import routers

from shopping_list.api.viewsets import ShoppingItemViewSet

routers = routers.DefaultRouter()

routers.register("shopping-items",ShoppingItemViewSet,basename="shopping-items")

urlpatterns = [
    path("api/",include(routers.urls)),
]