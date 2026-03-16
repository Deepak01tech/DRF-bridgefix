from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('public/',views.public_view,name='public_view'),
    path('private/',views.private_view,name='private_view'),
]