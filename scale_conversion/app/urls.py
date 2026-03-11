from django.urls import path
from .views import scale_conversion_view

urlpatterns= [
    path('',scale_conversion_view,name= 'unit-conversion')

]