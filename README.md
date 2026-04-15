# Projeto IoT - Monitoramento de Temperatura
echo "# Projeto IoT - Monitoramento de Temperatura 🌡️
Este projeto automatiza a ingestão e visualização de dados de sensores.
- **Banco de Dados:** PostgreSQL via Docker (Porta 5435)
- **Dashboard:** Streamlit" > README.md
# Projeto IoT - Monitoramento de Temperatura 🌡️

Este projeto automatiza a ingestão e visualização de dados de sensores de temperatura utilizando um pipeline de dados.

## 🚀 Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Banco de Dados:** PostgreSQL (via Docker na porta 5435)
- **Visualização:** Streamlit
- **Bibliotecas:** Pandas, SQLAlchemy, Psycopg2

## 🛠️ Instruções de Execução

### 1. Banco de Dados (Docker)
Para subir o banco de dados, utilize o comando:
`docker-compose up -d`

### 2. Ingestão de Dados (Python)
Para carregar os dados do CSV para o PostgreSQL, execute:
`python src/ingestion.py`

### 3. Visualização (Dashboard)
Para abrir o painel com os gráficos no navegador, execute:
`streamlit run src/dashboard.py`

## 💻 Código de Ingestão (ingestion.py)
```python
import pandas as pd
from sqlalchemy import create_engine

# Conexão com o banco Docker
engine = create_engine('postgresql://postgres:unifecaf123@localhost:5435/postgres')

# Carga dos dados
df = pd.read_csv('data/IOT-temp.csv')
df.to_sql('leituras_iot', engine, if_exists='replace', index=False)
print("Dados enviados com sucesso!")
