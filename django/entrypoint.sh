#!/bin/sh

echo "Waiting for postgres..."
# configura permissões de execução
chmod +x ./wait-for-postgres.sh
# chame o script wait-for-postgres.sh
./wait-for-postgres.sh
echo "PostgreSQL started"

# Criar o projeto Django se ele ainda não existir
if [ ! -f "./manage.py" ]; then
  django-admin startproject $NAME_PROJECT .
fi

# Aplicar migrações
python manage.py migrate

# Criar superuser do django, se não existir
# python manage.py create_superuser_django
python manage.py createsuperuser --noinput --username admin --email admin@example.com


# executa o "command" do service do docker-compose.yml que inicia o servidor Django
exec "$@"
