import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Estilo com CSS personalizado para deixar parecido com a imagem
st.markdown("""
    <style>
        .menu {
            background-color: #d3d3d3;
            padding: 10px;
            width: 200px;
            height: 500px;
            float: left;
        }
        .info {
            background-color: white;
            border: 1px solid black;
            padding: 10px;
            margin-left: 210px;
            height: 500px;
        }
        .title {
            background-color: #d5edcc;
            padding: 10px;
            font-weight: bold;
            font-size: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Título superior
st.markdown('<div class="title">CREDPRO2</div>', unsafe_allow_html=True)

# Layout da página
st.markdown('<div class="menu">', unsafe_allow_html=True)
st.markdown("**MENU DE OPÇÕES**")
menu = st.radio("", [
    "NOVO CLIENTE",
    "ACOMPANHAR VENDA",
    "RELATORIO DE VENDA",
    "ANEXAR DOCUMENTOS",
    "CCA",
    "CREDITO",
    "SAIR"
])
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="info"><strong>INFORMAÇÕES</strong><br><br>', unsafe_allow_html=True)

# Conteúdo baseado na opção escolhida
if menu == "NOVO CLIENTE":
    st.write("Formulário para cadastrar novo cliente.")
elif menu == "ACOMPANHAR VENDA":
    st.write("Painel de acompanhamento de vendas.")
elif menu == "RELATORIO DE VENDA":
    st.write("Relatórios disponíveis para análise.")
elif menu == "ANEXAR DOCUMENTOS":
    st.write("Upload de documentos aqui.")
elif menu == "CCA":
    st.write("Acesso ao CCA.")
elif menu == "CREDITO":
    st.write("Informações sobre crédito.")
elif menu == "SAIR":
    st.write("Você saiu do sistema.")

st.markdown('</div>', unsafe_allow_html=True)
