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
st.markdown("<p class='titulo'>Plataforma de Análise Automática de Dados</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitulo'>Converta arquivos CSV em análises completas e organizadas de forma rápida e prática.</p>", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# O QUE É
# ==========================================================
st.markdown("<p class='section-title'>Sobre a plataforma</p>", unsafe_allow_html=True)

st.write("""
Esta plataforma foi desenvolvida para permitir que qualquer pessoa analise arquivos CSV de forma simples,
mesmo sem conhecimentos avançados em programação ou estatística.

O sistema realiza automaticamente:

- Limpeza e organização dos dados  
- Detecção e correção de erros comuns  
- Geração de estatísticas básicas  
- Criação de gráficos de análise  
- Construção de dashboards interativos  
- Produção de insights automáticos  

Ela é útil para estudantes, empresas, profissionais de análise de dados e qualquer pessoa que trabalha com planilhas.
""")

# ==========================================================
# COMO FUNCIONA
# ==========================================================
st.markdown("<p class='section-title'>Como funciona</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("1º Passo", "Envio do arquivo CSV")
    st.write("O usuário envia um arquivo CSV. O sistema interpreta a estrutura e identifica possíveis problemas.")
    st.image(
        "https://raw.githubusercontent.com/Claudio577/apresentacao5/main/uploadelimpeza.png",
        caption="Upload e limpeza de dados"
    )

with col2:
    st.metric("2º Passo", "Processamento e limpeza")
    st.write("O sistema organiza colunas, ajusta tipos de dados, remove inconsistências e prepara o arquivo.")
    st.image(
        "https://raw.githubusercontent.com/Claudio577/apresentacao5/main/Automático%20de%20EDA.png",
        caption="Relatório automático de EDA"
    )

with col3:
    st.metric("3º Passo", "Análise e insights")
    st.write("Após o processamento, gráficos e insights são gerados automaticamente para facilitar a compreensão.")
    st.image(
        "https://raw.githubusercontent.com/Claudio577/apresentacao5/main/InsightsIA.png",
        caption="Geração de insights automáticos"
    )

# ==========================================================
# TECNOLOGIAS UTILIZADAS
# ==========================================================
st.markdown("<p class='section-title'>Tecnologias utilizadas</p>", unsafe_allow_html=True)

st.write("""
Este projeto utiliza ferramentas modernas de análise e visualização de dados:

**Python:** linguagem principal utilizada na lógica, limpeza de dados e geração de insights.  
**Pandas:** biblioteca responsável por manipulação, organização e tratamento dos dados do CSV.  
**Streamlit:** responsável por transformar o código Python em uma interface web interativa.  
**Plotly:** biblioteca utilizada na criação dos gráficos dinâmicos e dashboards.  
**Lógica de EDA automatizado:** código próprio que identifica problemas, estatísticas e padrões nos dados.  
**Técnicas simples de IA e análise estatística:** responsáveis por destacar informações relevantes nos insights.

Essas ferramentas juntas tornam possível uma experiência intuitiva, rápida e acessível para qualquer usuário.
""")

# ==========================================================
# FUNCIONALIDADES
# ==========================================================
st.markdown("<p class='section-title'>Funcionalidades principais</p>", unsafe_allow_html=True)

st.write("""
**Upload inteligente**  
O sistema aceita arquivos CSV simples ou complexos, mesmo com erros comuns.

**Limpeza automática de dados**  
Padroniza nomes de colunas, corrige formatos, remove espaços, trata valores inconsistentes e ajusta tipos.

**Geração automática de EDA (Exploração de Dados)**  
Estatísticas gerais, contagem de registros, identificação de valores nulos e distribuição dos dados.

**Dashboard interativo**  
Visualizações como histogramas, boxplots, gráficos categóricos e correlações entre variáveis.

**Insights automáticos**  
Identificação simplificada de padrões, comportamentos e tendências nos dados analisados.

**Exportação do arquivo tratado**  
O usuário pode baixar o CSV limpo após o processamento.
""")

