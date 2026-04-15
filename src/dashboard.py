import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Conexão com o banco de dados (Porta 5435 que você configurou)
engine = create_engine('postgresql://postgres:unifecaf123@localhost:5435/postgres')

st.set_page_config(page_title="Monitoramento IoT - UniFECAF", layout="wide")

st.title("🌡️ Painel de Monitoramento de Temperatura (IoT)")
st.markdown("Projeto desenvolvido para a disciplina de Engenharia de Dados.")

try:
    # Busca os dados do banco
    df = pd.read_sql('SELECT * FROM leituras_iot', engine)
    
    if not df.empty:
        # Mostra os números principais (Cards)
        col1, col2, col3 = st.columns(3)
        col1.metric("Temperatura Atual", f"{df['Hourly_Temp'].iloc[-1]}°C")
        col2.metric("Média Geral", f"{round(df['Hourly_Temp'].mean(), 2)}°C")
        col3.metric("Máxima Registrada", f"{df['Hourly_Temp'].max()}°C")

        # Desenha o Gráfico de Linha
        st.subheader("Variação da Temperatura ao Longo do Tempo")
        st.line_chart(df.set_index('Datetime')['Hourly_Temp'])
        
        # Mostra a tabela com os últimos dados
        st.subheader("Últimas Leituras do Sensor")
        st.dataframe(df.tail(10))
    else:
        st.warning("O banco de dados está vazio. Rode o script de ingestão primeiro!")

except Exception as e:
    st.error(f"Erro ao conectar no banco: {e}")