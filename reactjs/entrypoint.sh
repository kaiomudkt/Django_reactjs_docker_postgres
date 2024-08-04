#!/bin/bash

# Define o diretório de trabalho
REACT_APP_DIR="/reactjs/app"
# Verifica se o diretório do projeto React.js existe
if [ ! -d "$REACT_APP_DIR" ]; then
  echo "Criando o diretório do projeto React.js..."
  mkdir -p "$REACT_APP_DIR"
fi

# Verifica se o diretório do projeto React.js existe
if [ ! -d "$REACT_APP_DIR/node_modules" ]; then
  echo "Criando o projeto React.js..."
  npx create-react-app "$REACT_APP_DIR" || { echo "Falha ao criar o projeto React.js"; exit 1; }
else
  echo "O projeto React.js já existe. Iniciando o servidor..."
fi

# Define a variável de ambiente PORT
export PORT=${REACTJS_PORT}

# Navega para o diretório do projeto
cd "$REACT_APP_DIR" || exit 1

echo "Copiando package.json e package-lock.json..."
cp /reactjs/package*.json ./
echo "Instalando as dependências do projeto React.js..."
npm install || { echo "Falha ao instalar as dependências"; exit 1; }

# Inicia a aplicação
# executa o "command" do service do docker-compose.yml que inicia o servidor React.js
exec "$@"