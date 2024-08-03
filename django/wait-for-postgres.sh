#!/bin/sh
# wait-for-postgres.sh

# verificar seu esta pegando as variaveis de ambiente
# echo "POSTGRES_HOST: $POSTGRES_HOST"
# echo "POSTGRES_PORT: $POSTGRES_PORT"
# echo "POSTGRES_DB: $POSTGRES_DB"
# echo "POSTGRES_USER: $POSTGRES_USER"
# echo "POSTGRES_PASSWORD: $POSTGRES_PASSWORD"

set -e


until  psql  "postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST/postgres"  -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

echo "SELECT 'CREATE DATABASE $POSTGRES_DB' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = '$POSTGRES_DB')\gexec"| PGPASSWORD=$POSTGRES_PASSWORD psql -h  "$POSTGRES_HOST" -U  "$POSTGRES_USER"
echo "SELECT 'CREATE DATABASE credenciamento_teste' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'credenciamento_teste')\gexec"| PGPASSWORD=$POSTGRES_PASSWORD psql -h  "$POSTGRES_HOST" -U  "$POSTGRES_USER"

>&2 echo "Postgres is up - executing command"

echo "PostgreSQL started"
