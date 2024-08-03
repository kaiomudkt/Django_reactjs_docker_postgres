import uuid
from django.db import models

class Supplier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    logo = models.URLField()
    state = models.CharField(max_length=2)  # E.g., 'SP', 'RJ'
    cost_per_kwh = models.DecimalField(max_digits=10, decimal_places=4)
    min_kwh_limit = models.PositiveIntegerField()
    total_customers = models.PositiveIntegerField()
    average_rating = models.DecimalField(max_digits=3, decimal_places=2)
    status = models.CharField(
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

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)  # Associe um cliente a um usuário
    company_name = models.CharField(max_length=255)
    monthly_consumption = models.PositiveIntegerField()  # Consumo mensal em kWh
    status = models.CharField(
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

