from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from clarke.models import Supplier, Client, User

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'cost_per_kwh', 'min_kwh_limit', 'total_customers', 'average_rating', 'status')
    # list_display_links = ('name')
    search_fields = ('name', 'state')
    list_filter = ('state', 'status')
    ordering = ('name',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'user', 'monthly_consumption', 'status')
    # list_display_links = ('company_name')
    search_fields = ('company_name',)
    list_filter = ('status',)
    ordering = ('company_name',)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff')
    ordering = ('username',)
