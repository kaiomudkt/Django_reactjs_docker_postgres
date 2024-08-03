import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Supplier(models.Model):
    id: uuid.UUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name: str = models.CharField(max_length=255)
    logo: str = models.URLField()
    state: str = models.CharField(max_length=2)  # E.g., 'SP', 'RJ'
    cost_per_kwh: models.DecimalField = models.DecimalField(max_digits=10, decimal_places=4)
    min_kwh_limit: int = models.PositiveIntegerField()
    total_customers: int = models.PositiveIntegerField()
    average_rating: models.DecimalField = models.DecimalField(max_digits=3, decimal_places=2)
    status: str = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Active'),
            ('inactive', 'Inactive'),
            ('suspended', 'Suspended')
        ],
        default='active'
    )

    def __str__(self) -> str:
        """
        Retorna o nome do fornecedor.
        """
        return self.name

class User(AbstractUser):
    status: str = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Active'),
            ('inactive', 'Inactive'),
            ('banned', 'Banned')
        ],
        default='active'
    )

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

class Client(models.Model):
    id: uuid.UUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user: User = models.OneToOneField(User, on_delete=models.CASCADE)  # Associe um cliente a um usuário
    company_name: str = models.CharField(max_length=255)
    monthly_consumption: int = models.PositiveIntegerField()  # Consumo mensal em kWh
    status: str = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Active'),
            ('inactive', 'Inactive'),
            ('prospective', 'Prospective')  # Cliente potencial ou prospectivo
        ],
        default='active'
    )

    def __str__(self) -> str:
        """
        Retorna o nome da empresa do cliente.
        """
        return self.company_name

    def get_eligible_suppliers(self) -> models.QuerySet:
        """
        Retorna os fornecedores que atendem às necessidades do cliente com base no consumo mensal.

        Returns:
            models.QuerySet: Um queryset de fornecedores que têm um limite mínimo de kWh menor ou igual ao consumo mensal do cliente.
        """
        return Supplier.objects.filter(min_kwh_limit__lte=self.monthly_consumption, status='active')
