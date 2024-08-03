from django.core.management.base import BaseCommand
from django_seed import Seed
from clarke.models import Supplier, Client, Contract
from datetime import timedelta
import random

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **options):
        seeder = Seed.seeder()

        # Criar Suppliers
        seeder.add_entity(
            Supplier,
            10,
            {
                'name': lambda x: seeder.faker.company(),
                'logo': lambda x: seeder.faker.image_url(),
                'state': lambda x: seeder.faker.state_abbr(),
                'cnpj': lambda x: f'{seeder.faker.random_number(digits=8)}{seeder.faker.random_number(digits=4)}{seeder.faker.random_number(digits=2)}',
                'cost_per_kwh': lambda x: seeder.faker.pydecimal(left_digits=2, right_digits=2, positive=True),
                'min_kwh_limit': lambda x: seeder.faker.random_number(digits=3),
                'total_customers': lambda x: seeder.faker.random_number(digits=4),
                'average_rating': lambda x: seeder.faker.pydecimal(left_digits=3, right_digits=2, positive=True),
                'status': lambda x: seeder.faker.random_element(elements=('active', 'inactive', 'suspended')),
            }
        )
        seeder.execute()

        # Criar Clients
        seeder.add_entity(
            Client,
            10,
            {
                'company_name': lambda x: seeder.faker.company(),
                'cpf_cnpj': lambda x: seeder.faker.random_number(digits=14),
                'address': lambda x: seeder.faker.address(),
                'contact_name': lambda x: seeder.faker.name(),
                'contact_email': lambda x: seeder.faker.email(),
                'monthly_consumption': lambda x: seeder.faker.random_number(digits=3),
                'status': lambda x: seeder.faker.random_element(elements=('active', 'inactive', 'prospective')),
            }
        )
        seeder.execute()

        # Garantir que Supplier e Client existam
        suppliers = list(Supplier.objects.all())
        clients = list(Client.objects.all())

        if not suppliers or not clients:
            self.stdout.write(self.style.ERROR('Insufficient data to create contracts. Ensure that Supplier and Client data exist.'))
            return

        # Criar Contracts
        seeder.add_entity(
            Contract,
            10,
            {
                'client': lambda x: seeder.faker.random_element(elements=clients),
                'supplier': lambda x: seeder.faker.random_element(elements=suppliers),
                'contract_date': lambda x: seeder.faker.date_this_decade(),
                'expiration_date': lambda x: self.generate_expiration_date(
                    contract_date=seeder.faker.date_this_decade()
                ),
                'contract_value': lambda x: seeder.faker.pydecimal(left_digits=7, right_digits=2, positive=True),
                'terms_and_conditions': lambda x: seeder.faker.text(),
                'is_active': lambda x: seeder.faker.boolean(),
            }
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS('Successfully seeded database with sample data.'))

    def generate_expiration_date(self, contract_date):
        """
        Gera uma data de expiração que é sempre depois da data do contrato.

        Args:
            contract_date (datetime.date): Data do contrato.

        Returns:
            datetime.date: Data de expiração que é garantida para ser após a data do contrato.
        """
        days_to_add = random.randint(30, 730)  # 30 dias a 2 anos
        return contract_date + timedelta(days=days_to_add)
