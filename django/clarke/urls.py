from django.contrib import admin
from django.urls import path, include
from .views import ClientViewSet, ContractViewSet, SupplierViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('client', ClientViewSet, basename='Cliente')
router.register('contract', ContractViewSet, basename='Contrato')
router.register('supplier', SupplierViewSet, basename='Fornecedor')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
