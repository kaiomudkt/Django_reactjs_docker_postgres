# Django_reactjs_docker_postgres

Visão geral do projeto
- Docker-compose.yml orquestrando container Docker
- Docker para ambiente postgres, react.js e django
- configurando execução com arquivo entrypoint.sh
- arquivo .env para variaveis de ambiente

### Django
- api REST

### iniciando projeto

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


