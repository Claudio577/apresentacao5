import streamlit as st

# ==========================================================
# CONFIG DO SITE
# ==========================================================
st.set_page_config(
    page_title="Data Intelligence — Apresentação do Projeto",
    layout="wide",
    page_icon="📊"
)

# ==========================================================
# ESTILO (OPCIONAL)
# ==========================================================
st.markdown(
    """
    <style>
    .titulo {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: -10px;
    }
    .subtitulo {
        font-size: 22px;
        text-align: center;
        color: #555;
    }
    .section-title {
        font-size: 28px;
        margin-top: 40px;
        margin-bottom: 10px;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# HERO SECTION
# ==========================================================
st.markdown("<p class='titulo'>📊 Plataforma de Análise Automática de Dados</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitulo'>Transforme arquivos CSV em análises inteligentes — sem precisar saber programação.</p>", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# O QUE É
# ==========================================================
st.markdown("<p class='section-title'>💡 O que é esta plataforma?</p>", unsafe_allow_html=True)

st.write("""
É um sistema que permite qualquer pessoa — mesmo sem conhecimento técnico — analisar arquivos CSV 
com apenas alguns cliques.

Ela faz automaticamente:

- ✔ Limpeza e organização dos dados  
- ✔ Correção de erros  
- ✔ Geração de estatísticas  
- ✔ Criação de gráficos  
- ✔ Painéis interativos  
- ✔ Insights inteligentes  

Ideal para estudantes, empresas, analistas iniciantes e qualquer pessoa que trabalha com planilhas.
""")

# ==========================================================
# COMO FUNCIONA
# ==========================================================
st.markdown("<p class='section-title'>⚙️ Como funciona?</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("1️⃣ Passo", "Envie o CSV")
    st.write("O sistema lê e entende o arquivo — mesmo se estiver bagunçado.")

with col2:
    st.metric("2️⃣ Passo", "Limpeza automática")
    st.write("Corrige colunas, remove erros e padroniza tudo.")

with col3:
    st.metric("3️⃣ Passo", "Gere insights")
    st.write("Você recebe gráficos, análises e dashboards interativos.")

# ==========================================================
# FUNCIONALIDADES
# ==========================================================
st.markdown("<p class='section-title'>🧰 Funcionalidades</p>", unsafe_allow_html=True)

st.write("""
### 📂 Upload inteligente  
Aceita qualquer CSV — até quebrado.

### 🧹 Limpeza de dados  
Corrige colunas, tipos, espaços e erros comuns.

### 📊 Auto-EDA  
Estatísticas, contagem, distribuição e problemas encontrados.

### 📈 Dashboard interativo  
Histograma, boxplot, correlação, gráficos categóricos e muito mais.

### 🤖 Insights automáticos  
A plataforma indica padrões e tendências dos dados.

### 📥 Exportação  
Baixe seu arquivo limpo em 1 clique.
""")

# ==========================================================
# PRINTS / DEMONSTRAÇÃO
# ==========================================================
st.markdown("<p class='section-title'>🖼️ Demonstração visual</p>", unsafe_allow_html=True)

colA, colB = st.columns(2)

with colA:
    st.image("https://i.imgur.com/F8VQQ4m.png", caption="Tela de Dashboard (exemplo)")

with colB:
    st.image("https://i.imgur.com/ILZzEMF.png", caption="Exemplo de análise automática")

# (Você pode substituir pelas suas screenshots do app real)

# ==========================================================
# ACESSAR O SISTEMA
# ==========================================================
st.markdown("<p class='section-title'>🚀 Acesse o sistema</p>", unsafe_allow_html=True)

st.success("Clique abaixo para acessar o aplicativo completo:")

st.markdown("### 👉 [Abrir a plataforma de análise](https://SEU-APP-STREAMLIT.streamlit.app)")

st.caption("Substitua o link pelo endereço verdadeiro do seu app.")
