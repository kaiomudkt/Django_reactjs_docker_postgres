# Usar a imagem oficial do Node.js
FROM node:20-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /reactjs

# Copia o entrypoint.sh para dentro do container
COPY ./entrypoint.sh /entrypoint.sh

# Define permissões de execução para o script
RUN chmod +x /entrypoint.sh

# Copia o package.json e o package-lock.json (se existir)
# TODO: COPY package*.json ./

# Instala as dependências
# TODO: RUN npm install

# Copiar todo o código da aplicação para o diretório de trabalho
COPY . .

# Passa as variáveis para a aplicação React
# RUN echo "REACT_APP_API_URL=${REACTJS_APP_API_URL}" > .env.local
# RUN echo "PORT=${REACTJS_PORT}" >> .env.local

# Construir a aplicação React
# TODO: RUN npm run build

# Expõe a porta em que a aplicação será servida
EXPOSE "${REACTJS_PORT}"

# Define o entrypoint
ENTRYPOINT ["/entrypoint.sh"]
