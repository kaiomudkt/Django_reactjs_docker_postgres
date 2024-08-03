# django/clarke/admin.py

from django.contrib import admin
from .models import Supplier, Client

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'cost_per_kwh', 'min_kwh_limit', 'total_customers', 'average_rating', 'status')
    search_fields = ('name', 'state')
    list_filter = ('state', 'status')
    ordering = ('name',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'monthly_consumption', 'status')
    search_fields = ('company_name', 'status')
    list_filter = ('status',)
    ordering = ('company_name',)
