# user/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny
from .serializers import *
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics

# @api_view(['POST'])
# def login_view(request):
#     # Implemente manualmente o login usando SimpleJWT se não usar CBV.
#     pass

# @api_view(['POST'])
# def register_view(request):
#     data = request.data
#     try:
#         user = User.objects.create(
#             username=data['username'],
#             # email=data['email'],
#             password=make_password(data['password'])
#         )
#         serializer = UserSerializer(user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     except Exception as e:
#         return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

#Login User
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

#Register User
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

#api/profile  and api/profile/update
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getProfile(request):
#     user = request.user
#     serializer = ProfileSerializer(user, many=False)
#     return Response(serializer.data)

# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def updateProfile(request):
#     user = request.user
#     serializer = ProfileSerializer(user, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# #api/notes
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getNotes(request):
#     public_notes = Note.objects.filter(is_public=True).order_by('-updated')[:10]
#     user_notes = request.user.notes.all().order_by('-updated')[:10]
#     notes = public_notes | user_notes
#     serializer = NoteSerializer(notes, many=True)
#     return Response(serializer.data)