import uuid
from django.db import models
from datetime import date
from django.db.models import QuerySet
from django.conf import settings
from user.models import CustomUser


class Supplier(models.Model):
    """
    Modelo que representa um fornecedor de energia.

    Atributos:
        id (UUIDField): Identificador único do fornecedor.
        name (CharField): Nome do fornecedor.
        logo (URLField): URL do logotipo do fornecedor.
        state (CharField): Sigla do estado onde o fornecedor opera (por exemplo, 'SP', 'RJ').
        cnpj (CharField): CNPJ do fornecedor.
        cost_per_kwh (DecimalField): Custo por kWh cobrado pelo fornecedor.
        min_kwh_limit (PositiveIntegerField): Consumo mínimo em kWh exigido pelo fornecedor.
        total_customers (PositiveIntegerField): Número total de clientes atendidos pelo fornecedor.
        average_rating (DecimalField): Avaliação média do fornecedor (de 0 a 5).
        status (CharField): Status do fornecedor (ativo, inativo, suspenso).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    # logo = models.URLField()
    logo = models.ImageField(upload_to='logo/', null=True, blank=True)
    state = models.CharField(max_length=2)  # E.g., 'SP', 'RJ'
    cnpj = models.CharField(max_length=18, unique=True)  # Cadastro Nacional de Pessoa Jurídica
    cost_per_kwh = models.DecimalField(max_digits=10, decimal_places=4)
    min_kwh_limit = models.PositiveIntegerField()
    total_customers = models.PositiveIntegerField()
    average_rating = models.DecimalField(max_digits=5, decimal_places=2)
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

        Returns:
            str: Nome do fornecedor.
        """
        return self.name


class Client(models.Model):
    """
    Modelo que representa um cliente que consome energia.

    Atributos:
        id (UUIDField): Identificador único do cliente.
        company_name (CharField): Nome da empresa cliente.
        cpf_cnpj (CharField): CPF ou CNPJ do cliente.
        address (CharField): Endereço do cliente.
        contact_name (CharField): Nome da pessoa de contato no cliente.
        contact_email (EmailField): E-mail da pessoa de contato no cliente.
        monthly_consumption (PositiveIntegerField): Consumo mensal de energia em kWh.
        status (CharField): Status do cliente (ativo, inativo, prospectivo).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=255)
    cpf_cnpj = models.CharField(max_length=18, unique=True)  # CPF ou CNPJ do cliente
    address = models.CharField(max_length=255)  # Endereço do cliente
    contact_name = models.CharField(max_length=255)  # Nome da pessoa de contato
    contact_email = models.EmailField()  # E-mail da pessoa de contato
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

        Returns:
            str: Nome da empresa do cliente.
        """
        return self.company_name

    def get_eligible_suppliers(self) -> QuerySet:
        """
        Retorna os fornecedores que atendem às necessidades do cliente com base no consumo mensal.

        Returns:
            QuerySet: Um queryset de fornecedores que têm um limite mínimo de kWh menor ou igual ao consumo mensal do cliente.
        """
        return Supplier.objects.filter(min_kwh_limit__lte=self.monthly_consumption, status='active')


class Contract(models.Model):
    """
    Modelo que representa um contrato entre um cliente e um fornecedor.

    Atributos:
        id (UUIDField): Identificador único do contrato.
        client (ForeignKey): Referência ao cliente que assinou o contrato.
        supplier (ForeignKey): Referência ao fornecedor que assinou o contrato.
        contract_date (DateField): Data de assinatura do contrato.
        expiration_date (DateField): Data de expiração do contrato.
        contract_value (DecimalField): Valor total do contrato.
        terms_and_conditions (TextField): Termos e condições do contrato.
        is_active (BooleanField): Indica se o contrato está ativo ou não.
        billing_frequency (CharField): Frequência de faturamento do contrato (mensal, trimestral, anual).
        payment_terms (CharField): Condições de pagamento do contrato (ex: 30 dias após faturamento).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    contract_date = models.DateField()  # Data do contrato
    expiration_date = models.DateField()  # Data de expiração do contrato
    contract_value = models.DecimalField(max_digits=15, decimal_places=2)  # Valor total do contrato
    terms_and_conditions = models.TextField()  # Termos e condições do contrato
    is_active = models.BooleanField(default=True)  # Status do contrato
    billing_frequency = models.CharField(
        max_length=20,
        choices=[
            ('monthly', 'Monthly'),
            ('quarterly', 'Quarterly'),
            ('annually', 'Annually')
        ],
        default='monthly'
    )
    payment_terms = models.CharField(max_length=50)  # Condições de pagamento

    def __str__(self) -> str:
        """
        Retorna uma representação do relacionamento entre Client e Supplier.

        Returns:
            str: Representação do contrato entre o cliente e o fornecedor.
        """
        return f"Contract between {self.client.company_name} and {self.supplier.name}"

    def is_expired(self) -> bool:
        """
        Verifica se o contrato está expirado.

        Returns:
            bool: True se o contrato estiver expirado, False caso contrário.
        """
        return date.today() > self.expiration_date

class ResponsibleCompany(models.Model):
    """
    Modelo que representa a relação muitos-para-muitos entre usuários e fornecedores.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'supplier')

    def __str__(self):
        return f"{self.user.username} is responsible for {self.supplier.name}"
