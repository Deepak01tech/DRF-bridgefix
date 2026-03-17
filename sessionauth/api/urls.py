from django.urls import path

from .views import Mega_list

urlpatterns = [
    path('',Mega_list,name= 'Mega_list' ),
    
]