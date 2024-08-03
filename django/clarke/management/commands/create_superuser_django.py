from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **options):
        if User.objects.filter(username='admin').exists():
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))
            return

        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='password123'
        )
        self.stdout.write(self.style.SUCCESS('Superuser created successfully'))

        # Verifica a criação e a senha
        user = User.objects.get(username='admin')
        self.stdout.write(self.style.SUCCESS(f'Password check: {user.check_password("password123")}'))
