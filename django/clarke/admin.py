from django.contrib import admin
from .models import Supplier, Client, Contract

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """
    Configuração do painel administrativo para o modelo Supplier.
    """
    list_display = ('name', 'state', 'cost_per_kwh', 'min_kwh_limit', 'total_customers', 'average_rating', 'status')
    search_fields = ('name', 'state', 'cnpj')
    list_filter = ('state', 'status')
    ordering = ('name',)
    readonly_fields = ('id',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """
    Configuração do painel administrativo para o modelo Client.
    """
    list_display = ('company_name', 'cpf_cnpj', 'address', 'contact_name', 'contact_email', 'monthly_consumption', 'status')
    search_fields = ('company_name', 'cpf_cnpj', 'contact_email')
    list_filter = ('status',)
    ordering = ('company_name',)
    readonly_fields = ('id',)

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    """
    Configuração do painel administrativo para o modelo Contract.
    """
    list_display = ('client', 'supplier', 'contract_date', 'expiration_date', 'contract_value', 'is_active')
    search_fields = ('client__company_name', 'supplier__name', 'contract_date')
    list_filter = ('contract_date', 'expiration_date', 'is_active')
    ordering = ('contract_date',)
    readonly_fields = ('id',)
