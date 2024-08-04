from rest_framework import serializers
from .models import Supplier, Client, Contract

class SupplierSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Supplier.

    Campos serializados:
        - id: Identificador único do fornecedor.
        - name: Nome do fornecedor.
        - logo: URL do logotipo do fornecedor.
        - state: Sigla do estado onde o fornecedor opera.
        - cnpj: CNPJ do fornecedor.
        - cost_per_kwh: Custo por kWh cobrado pelo fornecedor.
        - min_kwh_limit: Consumo mínimo em kWh exigido pelo fornecedor.
        - total_customers: Número total de clientes atendidos pelo fornecedor.
        - average_rating: Avaliação média do fornecedor.
        - status: Status do fornecedor (ativo, inativo, suspenso).
    """
    class Meta:
        model = Supplier
        fields = [
            'id', 'name', 'logo', 'state', 'cnpj', 
            'cost_per_kwh', 'min_kwh_limit', 
            'total_customers', 'average_rating', 'status'
        ]


class ClientSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Client.

    Campos serializados:
        - id: Identificador único do cliente.
        - company_name: Nome da empresa cliente.
        - cpf_cnpj: CPF ou CNPJ do cliente.
        - address: Endereço do cliente.
        - contact_name: Nome da pessoa de contato no cliente.
        - contact_email: E-mail da pessoa de contato no cliente.
        - monthly_consumption: Consumo mensal de energia em kWh.
        - status: Status do cliente (ativo, inativo, prospectivo).
    """
    class Meta:
        model = Client
        fields = [
            'id', 'company_name', 'cpf_cnpj', 'address', 
            'contact_name', 'contact_email', 
            'monthly_consumption', 'status'
        ]


class ContractSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Contract.

    Campos serializados:
        - id: Identificador único do contrato.
        - client: Referência ao cliente que assinou o contrato.
        - supplier: Referência ao fornecedor que assinou o contrato.
        - contract_date: Data de assinatura do contrato.
        - expiration_date: Data de expiração do contrato.
        - contract_value: Valor total do contrato.
        - terms_and_conditions: Termos e condições do contrato.
        - is_active: Indica se o contrato está ativo ou não.
        - billing_frequency: Frequência de faturamento do contrato.
        - payment_terms: Condições de pagamento do contrato.
    """
    class Meta:
        model = Contract
        fields = [
            'id', 'client', 'supplier', 'contract_date', 
            'expiration_date', 'contract_value', 
            'terms_and_conditions', 'is_active', 
            'billing_frequency', 'payment_terms'
        ]
