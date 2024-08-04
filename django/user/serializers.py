from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import CustomUser
from django.core.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

# Serializer para o JWT com campos adicionais (se necessário)
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         # Adicionar claims customizadas
#         token['username'] = user.username
#         return token

# # Serializer para registro de usuários
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
#         return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...

        return token

def validate_password(password):
    # validação básica: a senha deve ter pelo menos 8 caracteres
    if len(password) < 8:
        raise ValidationError('Password must be at least 8 characters long.')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'password2', 'cpf', 'profile_picture')
        extra_kwargs = {
            'password': {'write_only': True},
            'profile_picture': {'required': False, 'allow_null': True}  # Torne o campo opcional
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            cpf=validated_data['cpf'],
            profile_picture=validated_data.get('profile_picture'),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

# class ProfileSerializer(serializers.ModelSerializer):
#     notes = NoteSerializer(many=True, read_only=True)

#     class Meta:
#         model = CustomUser
#         fields = '__all__'