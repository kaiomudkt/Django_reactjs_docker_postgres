# user/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer

# LoginView (FBV)
@api_view(['POST'])
def login_view(request):
    # Implemente manualmente o login usando SimpleJWT se não usar CBV.
    pass

# RegisterView (FBV)
@api_view(['POST'])
def register_view(request):
    data = request.data
    try:
        user = User.objects.create(
            username=data['username'],
            # email=data['email'],
            password=make_password(data['password'])
        )
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
