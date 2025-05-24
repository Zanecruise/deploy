#!/bin/bash

echo "🚀 Iniciando setup da API ScoreLab v2..."

# Clonar repositório
echo "📥 Clonando repositório..."
git clone https://github.com/foundlab/scorelab-api.git
cd scorelab-api || exit

# Instalar dependências
echo "📦 Instalando dependências..."
npm install

# Gerar arquivo .env
echo "⚙️ Criando arquivo .env..."
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

# Iniciar a aplicação
echo "🔥 Iniciando a API ScoreLab..."
npm run dev

echo "✅ Deploy completo. API rodando em http://localhost:3000"