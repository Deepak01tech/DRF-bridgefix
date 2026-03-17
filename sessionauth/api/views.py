# from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Mega
from .serializers import Megaserializer
from rest_framework import status


@api_view(['GET','POST'])
def Mega_list(request):
    if request.method == 'GET':
        dataf=Mega.objects.all()
        serializer=Megaserializer(dataf,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=Megaserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

