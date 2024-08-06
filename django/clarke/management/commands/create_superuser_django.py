from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Create a superuser and assign all groups and permissions'

    def handle(self, *args, **options):
        User = get_user_model()
        username = 'admin'
        email = 'admin@example.com'
        password = 'Password.123'
        client_group, _ = Group.objects.get_or_create(name='Client')
        supplier_group, _ = Group.objects.get_or_create(name='Supplier')
        
        # Verificar se o superusuário já existe
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'User {username} already exists'))
            return

        # Criar superusuário
        user = User.objects.create_superuser(username=username, email=email, password=password)
        user.groups.add(client_group)
        user.groups.add(supplier_group)
        # Adicionar superusuário a todos os grupos existentes
        all_groups = Group.objects.all()
        for group in all_groups:
            user.groups.add(group)
        
        # Conceder todas as permissões ao superusuário
        all_permissions = Permission.objects.all()
        for permission in all_permissions:
            user.user_permissions.add(permission)
        
        self.stdout.write(self.style.SUCCESS(f'Superuser {username} created successfully'))
        self.stdout.write(self.style.SUCCESS(f'Password check: {user.check_password(password)}'))
