import streamlit as st
import pandas as pd
import math
from pathlib import Path

import streamlit as st

# Remover espaço padrão do Streamlit
st.set_page_config(layout="wide")

# CSS customizado pra deixar o visual parecido com o Excel
st.markdown("""
    <style>
        .title-bar {
            background-color: #d5edcc;
            padding: 10px;
            font-weight: bold;
            font-size: 20px;
        }
        .menu-box {
            background-color: #d3d3d3;
            padding: 10px;
            height: 480px;
            border: 1px solid #aaa;
        }
        .info-box {
            background-color: white;
            padding: 10px;
            border: 1px solid black;
            height: 480px;
            overflow-y: auto;
        }
        .radio .stRadio > div {
            flex-direction: column;
        }
    </style>
""", unsafe_allow_html=True)

# Título da barra verde
st.markdown('<div class="title-bar">CREDPRO2</div>', unsafe_allow_html=True)

# Layout com colunas
col1, col2 = st.columns([1, 5])

with col1:
    st.markdown('<div class="menu-box"><strong>MENU DE OPÇÕES</strong></div>', unsafe_allow_html=True)
    menu = st.radio("", [
        "NOVO CLIENTE",
        "ACOMPANHAR VENDA",
        "RELATORIO DE VENDA",
        "ANEXAR DOCUMENTOS",
        "CCA",
        "CREDITO",
        "SAIR"
    ])

with col2:
    st.markdown('<div class="info-box"><strong>INFORMAÇÕES</strong><br><br>', unsafe_allow_html=True)

    # Conteúdo de cada opção
    if menu == "NOVO CLIENTE":
        st.write("Formulário para cadastro de novo cliente.")
    elif menu == "ACOMPANHAR VENDA":
        st.write("Acompanhamento de vendas em tempo real.")
    elif menu == "RELATORIO DE VENDA":
        st.write("Relatório de vendas por período.")
    elif menu == "ANEXAR DOCUMENTOS":
        st.write("Área para anexar documentos do cliente.")
    elif menu == "CCA":
        st.write("Acesso ao sistema CCA.")
    elif menu == "CREDITO":
        st.write("Análise de crédito.")
    elif menu == "SAIR":
        st.write("Encerrando sessão.")

    st.markdown('</div>', unsafe_allow_html=True)
