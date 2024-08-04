from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Seed the database with CustomUser data'

    def handle(self, *args, **options):
        fake = Faker()
        User = get_user_model()
        client_group, _ = Group.objects.get_or_create(name='Client')
        supplier_group, _ = Group.objects.get_or_create(name='Supplier')
        # Criar o usuário fixo para o grupo "Client"
        client_user = User(
            username='teste_client',
            email='teste_client@example.com',
            password='client_password',
            first_name='Teste',
            last_name='Client',
            cpf='12345678901',
        )
        client_user.set_password('client_password')
        client_user.save()
        client_user.groups.add(client_group)
        # Criar o usuário fixo para o grupo "Supplier"
        supplier_user = User(
            username='teste_supplier',
            email='teste_supplier@example.com',
            password='supplier_password',
            first_name='Teste',
            last_name='Supplier',
            cpf='12345678902',
        )
        supplier_user.set_password('supplier_password')
        supplier_user.save()
        supplier_user.groups.add(supplier_group)
        # Criar usuários aleatórios
        amount = 10
        for _ in range(amount):
            user = User(
                username=fake.user_name(),
                email=fake.email(),
                password=fake.password(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                cpf=fake.unique.random_number(digits=11),
            )
            user.set_password('password')
            user.save()
            # Adicionar usuários aleatórios a grupos aleatórios
            if fake.boolean():
                user.groups.add(client_group)
            else:
                user.groups.add(supplier_group)

        self.stdout.write(self.style.SUCCESS('Successfully seeded CustomUser data.'))
