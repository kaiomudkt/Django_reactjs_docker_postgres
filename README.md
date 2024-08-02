# Django_reactjs_docker_postgres

Visão geral do projeto
- Docker-compose.yml orquestrando container Docker
- Docker para ambiente postgres, react.js e django
- configurando execução com arquivo entrypoint.sh
- arquivo .env para variaveis de ambiente

### Django
- api REST

### iniciando projeto

$ sudo docker-compose down -v

$ sudo docker-compose up --build

$ sudo chown -R $(whoami):$(whoami) .

