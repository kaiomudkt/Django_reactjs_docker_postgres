from .models import Client, Contract, Supplier
from .serializers import ClientSerializer, ContractSerializer, SupplierSerializer, ListContractClientsSerializer, ListContractSupplierSerializer
from rest_framework import viewsets, generics

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

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
