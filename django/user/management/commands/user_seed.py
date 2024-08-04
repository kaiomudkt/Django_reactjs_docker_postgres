from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker

class Command(BaseCommand):
    help = 'Seed the database with CustomUser data'

    def handle(self, *args, **options):
        fake = Faker()
        User = get_user_model()
        amount = 10
        for _ in range(amount):
            user = User(
                username=fake.user_name(),
                email=fake.email(),
                password=fake.password(),  # Use um método de hash
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                cpf=fake.unique.random_number(digits=11),
            )
            user.set_password('password')  # Defina a senha padrão
            user.save()

        self.stdout.write(self.style.SUCCESS('Successfully seeded CustomUser data.'))
