from .models import Client, Contract, Supplier
from .serializers import ClientSerializer, ContractSerializer, SupplierSerializer, ListContractClientsSerializer, ListContractSupplierSerializer
from rest_framework import viewsets, generics, permissions

class IsClientOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_client or request.user.is_admin
    
class IsSupplierOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_supplier or request.user.is_admin

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsClientOrAdmin]
    def get_queryset(self):
        if self.request.user.is_client:
            return Client.objects.filter(pk=self.request.user.pk)
        return Client.objects.all()

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsSupplierOrAdmin]
    def get_queryset(self):
        if self.request.user.is_supplier:
            return Supplier.objects.filter(pk=self.request.user.pk)
        return Supplier.objects.all()

class ListContractClient(generics.ListAPIView):
    """
    Lista todos os contratos deste cliente, com seus respectivos fornecedores
    """
    def get_queryset(self):
        queryset = Contract.objects.filter(client_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListContractClientsSerializer   

class ListContractSupplier(generics.ListAPIView):
    """
    Lista todos os contratos deste fornecedor, com seus respectivos clientes 
    """
    def get_queryset(self):
        queryset = Contract.objects.filter(supplier_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListContractSupplierSerializer   

