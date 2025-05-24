#!/bin/bash

echo "🚀 Iniciando setup da API ScoreLab v2 com PM2..."

# Clonar repositório
git clone https://github.com/foundlab/scorelab-api.git
cd scorelab-api || exit

# Instalar dependências
npm install

# Criar .env
cat <<EOT >> .env
PORT=3000
MONGO_URI=mongodb+srv://user:pass@cluster.mongodb.net/scorelab
JWT_SECRET=foundlab_secret_key
ALCHEMY_API_KEY=your_alchemy_key
BITQUERY_API_KEY=your_bitquery_key
IPFS_PROJECT_ID=your_project_id
IPFS_SECRET=your_project_secret
IPFS_ENDPOINT=https://ipfs.infura.io:5001
ENGINE_VERSION=v2.3.1
EOT

# Validar variáveis
echo "✅ Validando variáveis .env..."
REQUIRED_VARS=(MONGO_URI JWT_SECRET ALCHEMY_API_KEY IPFS_PROJECT_ID IPFS_SECRET)
for VAR in "${REQUIRED_VARS[@]}"; do
  if ! grep -q "$VAR=" .env; then
    echo "❌ Variável $VAR não encontrada no .env"
    exit 1
  fi
done

# Instalar PM2 e iniciar app
npm install -g pm2
pm2 start src/index.js --name scorelab-api
pm2 save

echo "✅ API ScoreLab rodando em segundo plano com PM2."