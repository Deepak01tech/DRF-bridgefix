from django.urls import path
from .views import BookViewSet


urlpatterns = [
    
    path('',BookViewSet.as_view({'get': 'list', 'post': 'create', 'put':'update','patch':'partial_update','delete':'destroy'}), name='book-list'),
]

# """
#     A viewset that provides default `create()`, `retrieve()`, `update()`,
#     `partial_update()`, `destroy()` and `list()` actions.
#     """