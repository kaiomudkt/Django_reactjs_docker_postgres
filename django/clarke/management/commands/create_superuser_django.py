from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **options):
        if User.objects.filter(username='admin').exists():
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))
            return

        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin'
        )
        self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
