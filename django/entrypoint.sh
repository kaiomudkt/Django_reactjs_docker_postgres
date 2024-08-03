#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    echo "POSTGRES_HOST: $POSTGRES_HOST"
    echo "POSTGRES_PORT: $POSTGRES_PORT"

    while ! nc -w 5 -z $POSTGRES_HOST $POSTGRES_PORT; do
      echo "Waiting for the database to be ready..."
      sleep 1
    done

    echo "PostgreSQL started"
fi

# Criar o projeto Django se ele ainda não existir
if [ ! -f "./manage.py" ]; then
  django-admin startproject $NAME_PROJECT .
fi

# Aplicar migrações
python manage.py migrate

# Iniciar o servidor Django
exec "$@"
