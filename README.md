# Django_reactjs_docker_postgres

Visão geral do projeto
- Docker-compose.yml orquestrando container Docker
- Docker para ambiente postgres, react.js e django
- configurando execução com arquivo entrypoint.sh
- arquivo .env para variaveis de ambiente
- script wait-for-postgres.sh faz com que o django espere o postgres responder antes de tentar conectar
- script create_superuser_django.py automátiza a criação do superuser do Django
- nginx

### Django
- api REST

### iniciando projeto

crie o arquivo '.env' na raiz do projeto com base no '.env.example'

```bash
$ sudo docker-compose down -v
```

```bash
$ sudo docker-compose up --build
```

Arruma erro de permissao nos arquivos
```bash
$ sudo chown -R $(whoami):$(whoami) .
```

entra no container do django
```bash
$ sudo docker-compose exec service_backend /bin/bash
```

cria as migrations
```bash
$ sudo docker-compose exec service_backend /bin/bash -c "python manage.py makemigrations"
```

executando migrations
```bash
$ sudo docker-compose exec service_backend /bin/bash -c "python manage.py migrate"
```

```bash
$ sudo docker-compose exec service_backend /bin/bash -c "python manage.py showmigrations"
```

se ainda nao criou as migrations do modulo clarke
```bash
sudo docker-compose exec service_backend /bin/bash 
python manage.py makemigrations clarke
python manage.py migrate clarke
```

criar um super usuário no django
```bash 
$ sudo docker-compose exec service_backend /bin/bash -c "python manage.py createsuperuser"
```
