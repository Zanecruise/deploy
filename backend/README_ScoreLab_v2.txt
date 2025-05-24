# FoundLab ScoreLab API v2

## Descrição
ScoreLab é uma infraestrutura de reputação para carteiras on-chain, capaz de detectar sinais técnicos, calcular score reputacional, gerar NFTs de confiança e operar de forma modular com lógica determinística e reativa.

## Módulos Principais
- **Sentinela**: Monitora eventos em tempo real e aciona análises automaticamente.
- **Sherlock**: Motor analítico que coleta dados on-chain e atribui flags.
- **Score Engine (P(x))**: Calcula score baseado em ponderação de flags (determinística) e estimativas comportamentais (probabilísticas).
- **Mirror Engine**: Compara estados atuais com snapshots anteriores para verificar regressão ou evolução reputacional.
- **GasMonitor**: Detecta padrões de uso anormal de gas para flag de evasão/manipulação.
- **NFT Engine**: Gera NFTs com metadata reputacional, publica no IPFS.

## Endpoints REST
- `POST /analyze`: Inicia análise reputacional de uma carteira.
- `GET /score/:wallet`: Consulta o score e as flags de uma carteira.
- `POST /mint`: Gera NFT reputacional com metadados IPFS.
- `GET /nft/:wallet`: Consulta metadata NFT de uma carteira.
- `GET /flags`: Lista todas as flags possíveis com descrição e impacto.

## Tecnologias
- Node.js, Express
- MongoDB
- IPFS (via ipfs-http-client)
- ethers.js, Alchemy, Bitquery

## Segurança
- JWT para rotas sensíveis
- Rate Limiting por IP