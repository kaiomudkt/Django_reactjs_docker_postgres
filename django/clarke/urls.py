# project/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .views import ClientViewSet, ContractViewSet, SupplierViewSet, ListContractClient, ListContractSupplier

router = routers.DefaultRouter()
router.register('client', ClientViewSet, basename='client')
router.register('contract', ContractViewSet, basename='contract')
router.register('supplier', SupplierViewSet, basename='supplier')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('user.urls')),
    # path('', include('user.views')),
    path('client/<uuid:pk>/contract/', ListContractClient.as_view(), name='contracts_by_client'),
    path('supplier/<uuid:pk>/contract/', ListContractSupplier.as_view(), name='contracts_by_supplier'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
