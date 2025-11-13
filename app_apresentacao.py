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
# ESTILO PERSONALIZADO
# ==========================================================
st.markdown(
    """
    <style>
    
    /* ----------- TÍTULO PRINCIPAL ----------- */
    .titulo {
        font-size: 48px;
        font-weight: 800;
        text-align: center;
        margin-bottom: -5px;
        background: -webkit-linear-gradient(45deg, #007bff, #00c4ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* ----------- SUBTÍTULO ----------- */
    .subtitulo {
        font-size: 22px;
        text-align: center;
        color: #444;
        margin-bottom: 20px;
    }

    /* ----------- TÍTULOS DE SEÇÃO ----------- */
    .section-title {
        font-size: 30px;
        margin-top: 40px;
        margin-bottom: 10px;
        font-weight: 700;
        color: #0056b3;
        border-left: 6px solid #0056b3;
        padding-left: 10px;
    }

    /* ----------- TEXTO GERAL ----------- */
    .texto {
        font-size: 18px;
        color: #333;
        line-height: 1.6;
    }

    /* ----------- MÉTRICAS ----------- */
    .metric-label {
        font-size: 20px !important;
        font-weight: 600 !important;
        color: #0066cc !important;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# HERO SECTION
# ==========================================================
st.markdown("<p class='titulo'>Plataforma de Análise Automática de Dados</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitulo'>Converta arquivos CSV em análises completas, dashboards e insights de forma simples e rápida.</p>", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# O QUE É
# ==========================================================
st.markdown("<p class='section-title'>Sobre a plataforma</p>", unsafe_allow_html=True)

st.markdown("""
<div class='texto'>
Esta plataforma foi criada para ajudar qualquer pessoa — mesmo sem conhecimento técnico — a analisar arquivos CSV
de maneira eficiente e automatizada.

O sistema realiza automaticamente:

<br>• Limpeza e organização dos dados  
• Correção de erros  
• Geração de estatísticas  
• Criação de gráficos  
• Construção de dashboards interativos  
• Produção de insights automáticos  

Ideal para estudantes, empresas, iniciantes em análise de dados e qualquer pessoa que trabalha com planilhas.
</div>
""", unsafe_allow_html=True)

# ==========================================================
# COMO FUNCIONA
# ==========================================================
st.markdown("<p class='section-title'>Como funciona</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("1º Passo", "Envie o CSV")
    st.write("O sistema interpreta o arquivo e identifica possíveis erros.")
    st.image("https://raw.githubusercontent.com/Claudio577/apresentacao5/main/uploadelimpeza.png",
             caption="Upload e limpeza de dados")

with col2:
    st.metric("2º Passo", "Processamento e limpeza")
    st.write("Colunas e dados são padronizados, corrigidos e reorganizados.")
    st.image("https://raw.githubusercontent.com/Claudio577/apresentacao5/main/Automático%20de%20EDA.png",
             caption="Relatório automático de EDA")

with col3:
    st.metric("3º Passo", "Análises e insights")
    st.write("Gráficos, dashboards e insights são gerados automaticamente.")
    st.image("https://raw.githubusercontent.com/Claudio577/apresentacao5/main/InsightsIA.png",
             caption="Insights automáticos")

# ==========================================================
# TECNOLOGIAS UTILIZADAS
# ==========================================================
st.markdown("<p class='section-title'>Tecnologias utilizadas</p>", unsafe_allow_html=True)

st.markdown("""
<div class='texto'>
A plataforma foi desenvolvida com tecnologias modernas de análise e visualização:

<br>• <b>Python</b> — Linguagem principal da aplicação  
• <b>Pandas</b> — Manipulação, limpeza e organização dos dados  
• <b>Streamlit</b> — Construção da interface web interativa  
• <b>Plotly</b> — Gráficos dinâmicos e dashboards  
• <b>Rotinas próprias de EDA</b> — Identificação automática de padrões e problemas  
• <b>Algoritmos simples de IA</b> — Apoio na geração de insights

Essas ferramentas proporcionam uma experiência acessível e poderosa, mesmo para quem não tem experiência técnica.
</div>
""", unsafe_allow_html=True)

# ==========================================================
# FUNCIONALIDADES
# ==========================================================
st.markdown("<p class='section-title'>Funcionalidades principais</p>", unsafe_allow_html=True)

st.markdown("""
<div class='texto'>
<b>Upload inteligente</b><br>
Recebe arquivos CSV de diferentes formatos e estruturas.

<br><b>Limpeza automática</b><br>
Padroniza colunas, corrige inconsistências e organiza o conjunto de dados.

<br><b>Análise exploratória (EDA)</b><br>
Geração de estatísticas essenciais e informações sobre a distribuição dos dados.

<br><b>Dashboard interativo</b><br>
Gráficos atualizados automaticamente conforme o usuário explora os dados.

<br><b>Insights automáticos</b><br>
Apontamento de padrões, comparações relevantes e tendências importantes.

<br><b>Exportação</b><br>
Permite baixar o arquivo CSV já tratado.
</div>
""", unsafe_allow_html=True)

