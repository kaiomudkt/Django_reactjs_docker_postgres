# Usar a imagem oficial do Python
FROM python:3.10-slim

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Definir o diretório de trabalho no contêiner
WORKDIR /django

# Instalar dependências do sistema e o cliente PostgreSQL
RUN apt-get update && \
apt-get install -y \
libpq-dev \
netcat-openbsd \
postgresql-client \
&& rm -rf /var/lib/apt/lists/*

# Copiar o arquivo de requisitos e instalá-los
COPY requirements.txt /django/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar o entrypoint.sh
COPY entrypoint.sh /entrypoint.sh
# Torna o script executável
RUN chmod +x /entrypoint.sh
# Copiar script wait-for-postgres.sh
COPY wait-for-postgres.sh /wait-for-postgres.sh
# Torna o script executável
RUN chmod +x /wait-for-postgres.sh

# Copiar todo o código da aplicação para o diretório de trabalho
COPY . /django/

# Comando para rodar o entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
