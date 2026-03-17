from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework_response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication.models import Token

@api_view(['GET'])
@uthentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user=request.user
    return Response({
        "username":user.username,
        "email":user.email,
        "is_staff":user.is_staff,
    })


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def admin_panel(request):
    return Response({
        "message":f"wlcome to the admin panel,{request.user.username}"
    })
