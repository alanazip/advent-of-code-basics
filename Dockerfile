# Usar a imagem oficial do Node.js
FROM node:16

# Criar diretório de trabalho no container
WORKDIR /app

# Copiar o arquivo de dependências
COPY package*.json ./

# Instalar dependências
RUN npm install

# Copiar todo o código para o diretório de trabalho
COPY . .

# Expor a porta que o servidor irá usar
EXPOSE 3000

# Comando para iniciar o servidor
CMD ["node", "server.js"]