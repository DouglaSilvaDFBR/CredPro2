import streamlit as st

# Título da página
st.set_page_config(page_title="Sistema de Vendas", layout="wide")
st.title("Sistema de Gestão Comercial")

# Menu lateral
menu = st.sidebar.radio(
    "Menu",
    [
        "NOVO CLIENTE",
        "ACOMPANHAR VENDA",
        "RELATORIO DE VENDA",
        "ANEXAR DOCUMENTOS",
        "CCA",
        "CREDITO",
        "SAIR"
    ]
)

# Funções para cada página
def novo_cliente():
    st.header("Cadastro de Novo Cliente")
    # Adicione aqui os campos e lógica para cadastro

def acompanhar_venda():
    st.header("Acompanhamento de Vendas")
    # Lógica para visualizar vendas em andamento

def relatorio_venda():
    st.header("Relatório de Vendas")
    # Gerar e visualizar relatórios

def anexar_documentos():
    st.header("Anexar Documentos")
    uploaded_file = st.file_uploader("Escolha um arquivo para anexar")
    if uploaded_file:
        st.success(f"Arquivo '{uploaded_file.name}' enviado com sucesso!")

def cca():
    st.header("Controle de Crédito e Análise (CCA)")
    # Lógica de CCA

def credito():
    st.header("Solicitação de Crédito")
    # Lógica para solicitação e aprovação de crédito

def sair():
    st.warning("Você escolheu sair. Encerrando sessão...")

# Chamada da função de acordo com a opção do menu
if menu == "NOVO CLIENTE":
    novo_cliente()
elif menu == "ACOMPANHAR VENDA":
    acompanhar_venda()
elif menu == "RELATORIO DE VENDA":
    relatorio_venda()
elif menu == "ANEXAR DOCUMENTOS":
    anexar_documentos()
elif menu == "CCA":
    cca()
elif menu == "CREDITO":
    credito()
elif menu == "SAIR":
    sair()
