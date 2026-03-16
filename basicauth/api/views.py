from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny


# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return Response({"message":"this is public view accessible to everyone."})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def private_view(request):
    return Response({"message":f"hello,{request.user.username}.this is a private view accessible only to authenticated users."})

