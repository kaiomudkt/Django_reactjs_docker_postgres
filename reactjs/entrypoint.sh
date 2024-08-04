#!/bin/bash

# Define o diretório de trabalho
REACT_APP_DIR="/reactjs/app"
# Verifica se o diretório do projeto React.js existe
if [ ! -d "$REACT_APP_DIR" ]; then
  echo "Criando o diretório do projeto React.js..."
  mkdir -p "$REACT_APP_DIR"
fi

# Verifica se o diretório do projeto React.js existe
if [ ! -d /reactjs/node_modules ]; then
  echo "Criando o projeto React.js..."
  npx create-react-app "$REACT_APP_DIR" || { echo "Falha ao criar o projeto React.js"; exit 1; }
else
  echo "O projeto React.js já existe. Iniciando o servidor..."
fi

# Inicia a aplicação
# executa o "command" do service do docker-compose.yml que inicia o servidor React.js
exec "$@"