# django/user/models.py

from django.db import models
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.models import AbstractUser, Group, Permission

def validate_cpf(cpf):
    # Validação básica de CPF: deve ter 11 dígitos
    if not re.match(r'^\d{11}$', cpf):
        raise ValidationError('CPF must be exactly 11 digits.')

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_picture/', null=True, blank=True)
    cpf = models.CharField(max_length=11, unique=True, validators=[validate_cpf])
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True
    )