# projeto_cassandra

Projeto: ingestão de dados de vacinação no Cassandra (3 nós) usando Docker, pandas e DSBulk.
dataset utilizado: Kaggle > https://www.kaggle.com/datasets/jsppimentel99/vacinao-covid-19-brasil-05-23/data?select=Imu_COVID_RJ.csv
Numero total de registros: 43 milhoes.

## Conteúdo
- docker-compose.yml  (cluster Cassandra 3 nós)
- prepare_csv.py      (pré-processamento com pandas)
- scripts/dsbulk.sh   (comandos dsbulk)
- README.md

## Como rodar (resumo)
1. `docker compose up -d`
2. `python prepare_csv.py`
3. `./dsbulk load ...` 

# projeto_cassandra_imunizacao
