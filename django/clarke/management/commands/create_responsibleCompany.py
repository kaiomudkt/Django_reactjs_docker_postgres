from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from clarke.models import ResponsibleCompany, Supplier
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Create ResponsibleCompany entries for users and suppliers'

    def handle(self, *args, **options):
        User = get_user_model()
        
        # Obter os grupos
        client_group = Group.objects.get(name='Client')
        supplier_group = Group.objects.get(name='Supplier')
        
        # Obter todos os usuários
        users = User.objects.all()
        
        # Obter todos os fornecedores
        suppliers = Supplier.objects.all()

        if not suppliers:
            self.stdout.write(self.style.ERROR('No suppliers found. Ensure suppliers exist before creating ResponsibleCompany entries.'))
            return
        
        # Associa usuários com fornecedores aleatórios
        for user in users:
            if user.groups.filter(name='Supplier').exists():
                # Para usuários que são fornecedores, associar com um fornecedor aleatório
                supplier = suppliers.first()
                ResponsibleCompany.objects.get_or_create(user=user, supplier=supplier)
            elif user.groups.filter(name='Client').exists():
                # Para usuários que são clientes, você pode optar por associar com fornecedores aleatórios ou não associar
                if suppliers.exists():
                    supplier = suppliers.first()  # Ou selecione um fornecedor aleatório
                    ResponsibleCompany.objects.get_or_create(user=user, supplier=supplier)
        
        self.stdout.write(self.style.SUCCESS('Successfully created ResponsibleCompany entries for users.'))
