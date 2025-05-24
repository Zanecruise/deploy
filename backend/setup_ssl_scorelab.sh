#!/bin/bash

echo "🔐 Iniciando setup de HTTPS para ScoreLab API..."

# Instalar dependências
sudo apt update
sudo apt install nginx certbot python3-certbot-nginx -y

# Configurar domínio (ajuste conforme seu domínio real)
DOMAIN=api.foundlab.cloud
EMAIL=seu@email.com

# Configurar NGINX reverso
sudo tee /etc/nginx/sites-available/scorelab <<EOF
server {
    listen 80;
    server_name $DOMAIN;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
EOF

sudo ln -s /etc/nginx/sites-available/scorelab /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl restart nginx

# Gerar certificado SSL com Certbot
sudo certbot --nginx -d $DOMAIN --non-interactive --agree-tos -m $EMAIL

echo "✅ HTTPS ativado em https://$DOMAIN"