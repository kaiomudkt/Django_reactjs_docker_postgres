#!/bin/sh
# Especifica que o script deve ser executado usando o interpretador de comandos Bash.

echo "Waiting for postgres..."
# configura permissões de execução
chmod +x ./wait-for-postgres.sh
# chame o script wait-for-postgres.sh
./wait-for-postgres.sh
# ./wait-for-it.sh db:5432 --timeout=30 --strict -- echo "Database is up"
echo "PostgreSQL started successfully!"

# Criar o projeto Django se ele ainda não existir
if [ ! -f "./manage.py" ]; then
  django-admin startproject $NAME_PROJECT .
fi

echo "TYPE_ENVIRONMENT: $TYPE_ENVIRONMENT"
# Verifica se o tipo de ambiente é desenvolvimento
if [ "$TYPE_ENVIRONMENT" = "development" ]; then
  echo "Gerando migrations para todos os apps"
  python manage.py makemigrations
fi

# Aplicar migrações
python manage.py migrate

# Insere Seed
if [ "$TYPE_ENVIRONMENT" = "development" ]; then
  echo "Gerando Seed superuser"
  python manage.py create_superuser_django
  echo "Gerando Seed Supplier, Client e Contract"
  python manage.py seed_data
  echo "Gerando Seed CustomUser"
  python manage.py user_seed
fi

# executa o "command" do service do docker-compose.yml que inicia o servidor Django
exec "$@"
