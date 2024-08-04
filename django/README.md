

API REST Django

### Endpoints
- API REST relacionamento one-to-many
    - Lista todos os contratos deste cliente, com seus respectivos fornecedores
        - http://0.0.0.0:3001/client/f749c49d-2dfe-474c-a86c-270cc8676a94/contract/
    - Lista todos os contratos deste fornecedor, com seus respectivos clientes 
        - http://0.0.0.0:3001/supplier/5567054e-c8a9-4cee-b55d-9bf5b9ee357a/contract/
- User:
    - auth/login/
    - auth/register/



Arruma erro de permissao em todos os arquivos do projeto
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

se ainda nao criou as migrations do modulo clarke
```bash
sudo docker-compose exec service_backend /bin/bash 
python manage.py makemigrations clarke
python manage.py migrate clarke
```

exibe migrations
```bash
$ sudo docker-compose exec service_backend /bin/bash -c "python manage.py showmigrations"
```

Inserindo dados fakes no banco de dados
```bash 
$ sudo docker-compose exec service_backend /bin/bash -c "python manage.py seed_data"
```

criando novo módulo django
```bash 
$ sudo docker-compose exec service_backend /bin/bash -c "python manage.py startapp <user>"
```




