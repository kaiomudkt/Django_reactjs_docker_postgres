import factory
from factory import Faker
from .models import Supplier, Client, Contract

class SupplierFactory(factory.django.DjangoModelFactory):
    """
    Fábrica para criar instâncias de Supplier.
    """
    class Meta:
        model = Supplier

    name = Faker('company')
    logo = Faker('image_url')
    state = Faker('state_abbr')
    cost_per_kwh = Faker('pydecimal', left_digits=3, right_digits=4, positive=True)
    min_kwh_limit = Faker('random_int', min=1, max=1000)
    total_customers = Faker('random_int', min=1, max=10000)
    average_rating = Faker('pydecimal', left_digits=2, right_digits=1, positive=True)
    status = Faker('random_element', elements=['active', 'inactive', 'suspended'])

class ClientFactory(factory.django.DjangoModelFactory):
    """
    Fábrica para criar instâncias de Client.
    """
    class Meta:
        model = Client

    company_name = Faker('company')
    monthly_consumption = Faker('random_int', min=1, max=10000)
    status = Faker('random_element', elements=['active', 'inactive', 'prospective'])
    cpf_cnpj = Faker('cpf')  # Para clientes pessoa física, use Faker('cnpj') para pessoas jurídicas
    address = Faker('address')
    contact_name = Faker('name')
    contact_email = Faker('email')

class ContractFactory(factory.django.DjangoModelFactory):
    """
    Fábrica para criar instâncias de Contract.
    """
    class Meta:
        model = Contract

    client = factory.SubFactory(ClientFactory)
    supplier = factory.SubFactory(SupplierFactory)
    contract_date = Faker('date_this_year')
    expiration_date = Faker('date_this_year', offset_days=365)
    contract_value = Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    terms_and_conditions = Faker('text')
    is_active = Faker('boolean')
