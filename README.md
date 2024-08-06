## Django_reactjs_docker_postgres

Visão geral do projeto
- [FEITO] Docker-compose.yml orquestrando container Docker
- [FEITO] Docker para ambiente postgres, react.js e django
- [FEITO] configurando execução de cada ambiente com arquivo entrypoint.sh
    - [FEITO] cria e executa migration
    - [FEITO] distinção de ambiente Desenvolvimento de produção e testes
- [FEITO] arquivo .env para variaveis de ambiente
- [FEITO] script.sh wait-for-postgres.sh faz com que o django espere o postgres responder antes de tentar conectar
- [FEITO] script.py seed create_superuser_django.py automátiza a criação do superuser do Django
- [FEITO] script.py seed para criar users fake
- [FEITO] script.py seed para criar Clients, Suppliers, Contracts e ResponsibleCompany
- [FEITO] API Rest CRUD Clients, Suppliers, Contracts
- [FEITO] integração backend com banco de dados via network docker-compose.yml
- [FEITO] integração backend com frontend (CORS)
- [FAZER] API Rest CRUD ResponsibleCompany
- [FAZER] Model ResponsibleClient (usuário resposável pelo cliente)
- [FEITO] página/telas login, home, listagem de Suppliers, sidebar
- [FAZER] página/telas Client, Contracts e ResponsibleCompany
- [FAZER] nginx
- Django API REST
- [FEITO] autenticação JWT
- [FEITO] controle de permissoes por grupo de acesso (admin, client e suplier)
- [FAZEE] Teste automátizados no Django

## Regras de negócio
- Cliente pode ser PF ou PJ (cpf/cnpj)
- Fornecedor é PJ (CNPJ) 
- Um cliente pode receber energia de varios fornecedores
- Um fornecedor pode ter varios clientes
- Um cliente pode ter varios usuários responsáveis
- Um fornecedor pode ter vários responsáveis
- Somente o responsável ou superadmin pode ver dados privados 
- Cliente pode fazer cotação com varias fornecedores
- Cliente pode ter vários contratos com fornecedores e vice e versa

### fluxo do usuário
1º Usuário deve criar uma conta, depois criar um cliente ou um fornecedor
2º Usuário só pode alterar dados do cliente ou fornecedor que ele for responsável
3º Usuário faz orçamento (filtro na tela)
4º Cliente manifesta interesse em fornecedor criando novo contrato
5º Fornecedor deve aceitar o contrato com o Cliente
6º contrato firmado, todo mês o sistema irá gerar cobrança do cliente para debitar para o Fornecedor


## iniciando projeto

Arruma erro de permissao em todos os arquivos do projeto
```bash
$ sudo chown -R $(whoami):$(whoami) .
```

crie o arquivo '.env' na raiz do projeto com base no '.env.example'

```bash
$ sudo docker-compose down -v
```

```bash
$ sudo docker-compose up --build
```

criar um super usuário no django
```bash 
$ sudo docker-compose exec service_backend /bin/bash -c "python manage.py createsuperuser"
```

