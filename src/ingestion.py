import pandas as pd
from sqlalchemy import create_engine

# Aqui avisamos o Python onde o banco de dados está
engine = create_engine('postgresql://postgres:unifecaf123@localhost:5435/postgres')

def carregar_dados():
    print("Lendo o arquivo de temperatura...")
    # Ele vai procurar o arquivo na pasta data
    df = pd.read_csv('data/IOT-temp.csv')
    
    # Organiza os dados para o banco entender
    df.to_sql('leituras_iot', engine, if_exists='replace', index=False)
    print("Dados enviados para o banco com sucesso!")

if __name__ == "__main__":
    carregar_dados()
