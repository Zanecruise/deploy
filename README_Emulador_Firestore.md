
# 🚀 FoundLab FullStack + Orchestrator – Setup Local com Emulador Firestore

Este README guia você a rodar o projeto **localmente** usando o **Emulador do Firestore**, poupando créditos na nuvem e agilizando o desenvolvimento.

---

## 1. Pré-requisitos

- **Node.js** (v16+)
- **npm** ou **yarn**
- **Docker** (opcional, se você usar containers)
- **Firebase CLI**  
  ```bash
  npm install -g firebase-tools
  ```

---

## 2. Configurar o Emulador do Firestore

1. **Inicializar seu projeto Firebase**  
   Se ainda não fez:
   ```bash
   firebase init
   ```
   - Selecione **Firestore** e **Emulators**  
   - Escolha pastas e regras default (ENTER)

2. **Iniciar só o Emulador do Firestore**  
   ```bash
   firebase emulators:start --only firestore
   ```
   - URL padrão da interface web: http://localhost:8080  
   - Endpoint gRPC/HTTP para SDK: `localhost:8080`

---

## 3. Configurar seu Código Node.js

No seu entrypoint (ex: `index.js`, `app.js`, ou `SherlockCore.js`), substitua a inicialização do Admin SDK por:

```js
const admin = require('firebase-admin');

if (process.env.NODE_ENV === 'development') {
  admin.initializeApp({
    projectId: 'foundlab-dev',               // ID fictício para o emulador
    credential: admin.credential.applicationDefault(), 
    databaseURL: 'http://localhost:8080'     // Endereço do emulador Firestore
  });
  console.log('🔥 Conectado ao Emulador Firestore (localhost:8080)');
} else {
  admin.initializeApp({
    // Suas configs de produção
  });
  console.log('☁️ Conectado ao Firestore em Produção');
}

const db = admin.firestore();
// … seu código de leitura/escrita no Firestore …
```

> **Dica:**  
> - Certifique-se de definir `NODE_ENV=development` no seu `.env` ou script de start local.  
> - Não exponha esse snippet em produção.

---

## 4. Rodar o Projeto Localmente

1. **Instalar dependências**  
   ```bash
   npm install
   # ou
   yarn install
   ```

2. **Definir variável de ambiente**  
   ```bash
   export NODE_ENV=development
   ```

3. **Iniciar o Emulador** (se ainda não está rodando)  
   ```bash
   firebase emulators:start --only firestore
   ```

4. **Rodar a aplicação**  
   ```bash
   npm start
   # ou
   yarn start
   ```
   - Sua API estará disponível em `http://localhost:8080` (ou na porta configurada).

---

## 5. Docker (Opcional)

Se preferir containerizar:

```dockerfile
# Dockerfile
FROM node:16
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
ENV NODE_ENV=development
CMD ["npm", "start"]
```

```bash
docker build -t foundlab-local .
docker run -it -p 8080:8080 foundlab-local
```

> **Nota:** Ainda será necessário rodar o emulador localmente (fora do container) ou dentro de outro container Firebase.

---

## 6. Próximos Passos

- Quando pronto para produção, remova o bloco de emulador e defina `NODE_ENV=production`.  
- Ajuste `admin.initializeApp({ /* suas configs do Firebase */ })`.  
- Faça deploy em Cloud Run ou outro serviço com credenciais de produção.

---

**Bora codar, economizar créditos e lançar esse MVP FoundLab no ritmo de FoundLab!** 🚀
