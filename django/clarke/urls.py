from django.contrib import admin
from django.urls import path, include
from .views import ClientViewSet, ContractViewSet, SupplierViewSet, ListContractClient, ListContractSupplier
from rest_framework import routers

router = routers.DefaultRouter()
router.register('client', ClientViewSet, basename='Cliente')
router.register('contract', ContractViewSet, basename='Contrato')
router.register('supplier', SupplierViewSet, basename='Fornecedor')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('client/<uuid:pk>/contract/', ListContractClient.as_view()),
    path('supplier/<uuid:pk>/contract/', ListContractSupplier.as_view()),
]
