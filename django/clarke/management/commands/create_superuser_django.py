from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.management import call_command
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **options):
        help = 'Create a superuser with predefined credentials'
        User = get_user_model() 
        username = 'admin'
        email = 'admin@example.com'
        password = 'Password.123'
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING('User {username} already exists'))
            return
        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS(f'Superuser {username} created successfully'))
        # Verifica a criação e a senha
        user = User.objects.get(username=username)
        self.stdout.write(self.style.SUCCESS(f'Password check: {user.check_password(password)}'))
