# projeto_cassandra

Projeto: ingestão de dados de vacinação no Cassandra (3 nós) usando Docker, pandas e DSBulk.

## Conteúdo
- docker-compose.yml  (cluster Cassandra 3 nós)
- prepare_csv.py      (pré-processamento com pandas)
- scripts/dsbulk.sh   (comandos dsbulk)
- README.md

## Como rodar (resumo)
1. `docker compose up -d`
2. `python prepare_csv.py`
3. `./dsbulk load ...` (ver scripts/dsbulk.sh)

# projeto_cassandra_imunizacao
