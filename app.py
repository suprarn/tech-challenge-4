"""Aplicação Streamlit para diagnóstico preditivo de obesidade.

Sistema de apoio à decisão médica desenvolvido para o Tech Challenge 4
FIAP/POSTECH Data Analytics.

Páginas:
1. Sistema Preditivo - Formulário para predição de nível de obesidade
2. Dashboard Analítico - Insights e visualizações dos dados
3. Sobre o Projeto - Informações sobre metodologia e modelo
"""

import pickle
from pathlib import Path

import pandas as pd
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Sistema de Diagnóstico de Obesidade",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Caminhos
PROJECT_ROOT = Path(__file__).resolve().parent
MODEL_PATH = PROJECT_ROOT / "modelo.pkl"
ENCODER_PATH = PROJECT_ROOT / "label_encoder.pkl"
PLOTS_DIR = PROJECT_ROOT / "plots"


@st.cache_resource
def carregar_modelo():
    """Carrega o modelo e o encoder do disco."""
    with open(MODEL_PATH, "rb") as f:
        modelo = pickle.load(f)
    with open(ENCODER_PATH, "rb") as f:
        encoder = pickle.load(f)
    return modelo, encoder


# Descrições amigáveis para os níveis de obesidade
DESCRICOES_OBESIDADE = {
    "Insufficient_Weight": {
        "nome": "Peso Insuficiente",
        "cor": "#3498db",
        "descricao": "O paciente apresenta peso abaixo do considerado saudável para sua altura.",
        "recomendacao": "Recomenda-se avaliação nutricional para identificar possíveis deficiências e elaborar plano alimentar adequado.",
    },
    "Normal_Weight": {
        "nome": "Peso Normal",
        "cor": "#27ae60",
        "descricao": "O paciente está dentro da faixa de peso considerada saudável.",
        "recomendacao": "Manter hábitos saudáveis de alimentação e atividade física.",
    },
    "Overweight_Level_I": {
        "nome": "Sobrepeso Nível I",
        "cor": "#f39c12",
        "descricao": "O paciente apresenta sobrepeso leve, com risco moderado de complicações.",
        "recomendacao": "Recomenda-se reeducação alimentar e aumento da atividade física.",
    },
    "Overweight_Level_II": {
        "nome": "Sobrepeso Nível II",
        "cor": "#e67e22",
        "descricao": "O paciente apresenta sobrepeso significativo, com risco elevado.",
        "recomendacao": "Acompanhamento nutricional e médico recomendado. Considerar programa estruturado de perda de peso.",
    },
    "Obesity_Type_I": {
        "nome": "Obesidade Tipo I",
        "cor": "#e74c3c",
        "descricao": "Obesidade grau I identificada. Risco aumentado para doenças cardiovasculares e metabólicas.",
        "recomendacao": "Intervenção médica e nutricional recomendada. Avaliação de comorbidades.",
    },
    "Obesity_Type_II": {
        "nome": "Obesidade Tipo II",
        "cor": "#c0392b",
        "descricao": "Obesidade grau II (severa). Alto risco para complicações de saúde.",
        "recomendacao": "Tratamento multidisciplinar urgente. Considerar avaliação para intervenção cirúrgica.",
    },
    "Obesity_Type_III": {
        "nome": "Obesidade Tipo III",
        "cor": "#8e44ad",
        "descricao": "Obesidade grau III (mórbida). Risco muito elevado para a saúde.",
        "recomendacao": "Encaminhamento urgente para equipe multidisciplinar. Avaliação prioritária para cirurgia bariátrica.",
    },
}

# Labels em português para os campos
LABELS_PT = {
    "Gender": "Gênero",
    "Age": "Idade (anos)",
    "Height": "Altura (m)",
    "Weight": "Peso (kg)",
    "family_history": "Histórico familiar de sobrepeso",
    "FAVC": "Consumo frequente de alimentos calóricos",
    "FCVC": "Frequência de consumo de vegetais (1-3)",
    "NCP": "Número de refeições principais por dia",
    "CAEC": "Consumo de alimentos entre refeições",
    "SMOKE": "Hábito de fumar",
    "CH2O": "Consumo diário de água (1-3)",
    "SCC": "Monitora consumo de calorias",
    "FAF": "Frequência de atividade física (0-3)",
    "TUE": "Tempo usando dispositivos eletrônicos (0-2)",
    "CALC": "Consumo de álcool",
    "MTRANS": "Meio de transporte principal",
}


def pagina_predicao():
    """Página do sistema preditivo."""
    st.title("🩺 Sistema Preditivo de Obesidade")
    st.markdown("---")
    st.markdown(
        """
        ### Ferramenta de Apoio à Decisão Médica
        
        Insira os dados do paciente abaixo para obter uma predição do nível de obesidade
        baseada em fatores comportamentais, genéticos e de estilo de vida.
        """
    )

    modelo, encoder = carregar_modelo()

    # Formulário dividido em colunas
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("📋 Dados Pessoais")
        gender = st.selectbox("Gênero", ["Female", "Male"], format_func=lambda x: "Feminino" if x == "Female" else "Masculino")
        age = st.number_input("Idade (anos)", min_value=14, max_value=80, value=25)
        height = st.number_input("Altura (m)", min_value=1.40, max_value=2.20, value=1.70, step=0.01)
        weight = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0, value=70.0, step=0.5)
        family_history = st.selectbox(
            "Histórico familiar de sobrepeso",
            ["yes", "no"],
            format_func=lambda x: "Sim" if x == "yes" else "Não",
        )

    with col2:
        st.subheader("🍎 Hábitos Alimentares")
        favc = st.selectbox(
            "Consumo frequente de alimentos calóricos",
            ["yes", "no"],
            format_func=lambda x: "Sim" if x == "yes" else "Não",
        )
        fcvc = st.slider("Frequência de consumo de vegetais", 1.0, 3.0, 2.0, 0.1, help="1=Raramente, 2=Às vezes, 3=Sempre")
        ncp = st.slider("Refeições principais por dia", 1.0, 4.0, 3.0, 0.5)
        caec = st.selectbox(
            "Consumo entre refeições",
            ["no", "Sometimes", "Frequently", "Always"],
            format_func=lambda x: {"no": "Não", "Sometimes": "Às vezes", "Frequently": "Frequentemente", "Always": "Sempre"}[x],
        )
        calc = st.selectbox(
            "Consumo de álcool",
            ["no", "Sometimes", "Frequently", "Always"],
            format_func=lambda x: {"no": "Não", "Sometimes": "Às vezes", "Frequently": "Frequentemente", "Always": "Sempre"}[x],
        )

    with col3:
        st.subheader("🏃 Estilo de Vida")
        smoke = st.selectbox("Hábito de fumar", ["no", "yes"], format_func=lambda x: "Sim" if x == "yes" else "Não")
        ch2o = st.slider("Consumo diário de água", 1.0, 3.0, 2.0, 0.1, help="1=<1L, 2=1-2L, 3=>2L")
        scc = st.selectbox("Monitora calorias", ["no", "yes"], format_func=lambda x: "Sim" if x == "yes" else "Não")
        faf = st.slider("Atividade física semanal", 0.0, 3.0, 1.0, 0.1, help="0=Nenhuma, 1=1-2x, 2=3-4x, 3=5x+")
        tue = st.slider("Tempo em eletrônicos (h/dia)", 0.0, 2.0, 1.0, 0.1, help="0=0-2h, 1=3-5h, 2=>5h")
        mtrans = st.selectbox(
            "Transporte principal",
            ["Public_Transportation", "Automobile", "Walking", "Bike", "Motorbike"],
            format_func=lambda x: {
                "Public_Transportation": "Transporte Público",
                "Automobile": "Carro",
                "Walking": "A pé",
                "Bike": "Bicicleta",
                "Motorbike": "Moto",
            }[x],
        )

    st.markdown("---")

    # Botão de predição
    if st.button("🔍 Realizar Diagnóstico", type="primary", use_container_width=True):
        # Calcular BMI
        bmi = weight / (height**2)

        # Montar DataFrame
        dados = pd.DataFrame(
            [
                {
                    "Gender": gender,
                    "Age": age,
                    "Height": height,
                    "Weight": weight,
                    "family_history": family_history,
                    "FAVC": favc,
                    "FCVC": fcvc,
                    "NCP": ncp,
                    "CAEC": caec,
                    "SMOKE": smoke,
                    "CH2O": ch2o,
                    "SCC": scc,
                    "FAF": faf,
                    "TUE": tue,
                    "CALC": calc,
                    "MTRANS": mtrans,
                    "BMI": bmi,
                }
            ]
        )

        # Predição
        pred_encoded = modelo.predict(dados)
        pred_label = encoder.inverse_transform(pred_encoded)[0]
        info = DESCRICOES_OBESIDADE[pred_label]

        # Exibir resultado
        st.markdown("---")
        st.markdown("## 📊 Resultado do Diagnóstico")

        col_res1, col_res2 = st.columns([1, 2])

        with col_res1:
            st.markdown(
                f"""
                <div style="
                    background-color: {info['cor']}; 
                    padding: 30px; 
                    border-radius: 15px; 
                    text-align: center;
                    color: white;
                ">
                    <h2 style="margin: 0; color: white;">{info['nome']}</h2>
                    <p style="margin: 10px 0 0 0; font-size: 14px;">IMC calculado: {bmi:.1f}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col_res2:
            st.markdown(f"### Avaliação Clínica")
            st.markdown(f"**Diagnóstico:** {info['descricao']}")
            st.markdown(f"**Recomendação:** {info['recomendacao']}")

        st.info("⚕️ Este é um sistema de apoio à decisão. O diagnóstico final deve ser realizado por um profissional de saúde.")


def pagina_dashboard():
    """Página do dashboard analítico."""
    st.title("📈 Dashboard Analítico")
    st.markdown("---")
    st.markdown(
        """
        ### Insights sobre Fatores de Risco para Obesidade
        
        Visualizações baseadas na análise exploratória do dataset utilizado para treinamento do modelo.
        """
    )

    # Verificar se os gráficos existem
    if not PLOTS_DIR.exists():
        st.error("Diretório de gráficos não encontrado. Execute a EDA primeiro.")
        return

    # Tabs para organizar os gráficos
    tab1, tab2, tab3 = st.tabs(["📊 Distribuição do Target", "🔗 Análise Bivariada", "📉 Correlações"])

    with tab1:
        st.subheader("Distribuição dos Níveis de Obesidade na População")
        img_path = PLOTS_DIR / "1_target_distribution.png"
        if img_path.exists():
            st.image(str(img_path), use_container_width=True)
            st.markdown(
                """
                **Insights:**
                - A distribuição é relativamente balanceada entre os 7 níveis de obesidade
                - Obesidade Tipo I é a classe mais frequente (~17%)
                - Peso normal e insuficiente representam cerca de 26% da amostra
                """
            )
        else:
            st.warning("Gráfico não encontrado.")

    with tab2:
        st.subheader("Fatores de Risco por Nível de Obesidade")

        # Seletor de gráfico
        graficos_bivar = {
            "IMC (BMI)": "2_bivar_bmi_vs_obesity.png",
            "Peso": "2_bivar_weight_vs_obesity.png",
            "Idade": "2_bivar_age_vs_obesity.png",
            "Atividade Física": "2_bivar_faf_vs_obesity.png",
            "Histórico Familiar": "2_bivar_family_history_vs_obesity.png",
            "Consumo de Alimentos Calóricos": "2_bivar_favc_vs_obesity.png",
            "Transporte": "2_bivar_mtrans_vs_obesity.png",
        }

        selecionado = st.selectbox("Selecione o fator de risco:", list(graficos_bivar.keys()))
        img_path = PLOTS_DIR / graficos_bivar[selecionado]
        if img_path.exists():
            st.image(str(img_path), use_container_width=True)

    with tab3:
        st.subheader("Matriz de Correlação entre Variáveis Numéricas")
        img_path = PLOTS_DIR / "3_correlation_heatmap.png"
        if img_path.exists():
            st.image(str(img_path), use_container_width=True)
            st.markdown(
                """
                **Insights:**
                - Forte correlação entre Peso e BMI (esperado)
                - Correlação moderada entre Idade e Peso
                - Atividade física (FAF) tem correlação negativa com peso
                """
            )
        else:
            st.warning("Gráfico não encontrado.")

    # Métricas resumidas
    st.markdown("---")
    st.subheader("📋 Métricas do Modelo")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Acurácia", "99.04%", "Meta: 75%")
    col2.metric("Precision Média", "0.99")
    col3.metric("Recall Médio", "0.99")
    col4.metric("F1-Score Médio", "0.99")


def pagina_sobre():
    """Página sobre o projeto."""
    st.title("ℹ️ Sobre o Projeto")
    st.markdown("---")

    st.markdown(
        """
        ## Tech Challenge Fase 4 - FIAP/POSTECH Data Analytics
        
        ### 🎯 Objetivo
        Desenvolver um sistema de Machine Learning para auxiliar profissionais de saúde
        no diagnóstico preditivo de níveis de obesidade, considerando a natureza 
        multifatorial desta condição médica.
        
        ### 🔬 Metodologia
        
        1. **Análise Exploratória de Dados (EDA)**
           - Análise univariada e bivariada de 17 variáveis
           - Identificação de padrões e correlações
           - Criação da feature BMI (Índice de Massa Corporal)
        
        2. **Engenharia de Atributos**
           - StandardScaler para variáveis numéricas
           - OrdinalEncoder para CAEC e CALC
           - OneHotEncoder para variáveis categóricas nominais
        
        3. **Modelagem**
           - Algoritmo: Random Forest Classifier
           - Validação: Stratified 5-Fold Cross-Validation
           - Métricas: Accuracy, Precision, Recall, F1-Score
        
        ### 📊 Resultados
        
        | Métrica | Valor |
        |---------|-------|
        | Acurácia (CV) | 98.86% |
        | Acurácia (Teste) | 99.04% |
        | Precision Média | 0.99 |
        | Recall Médio | 0.99 |
        
        ### 🛠️ Stack Tecnológica
        - Python, Pandas, NumPy
        - Scikit-learn
        - Matplotlib, Seaborn
        - Streamlit
        
        ### 📁 Repositório
        O código completo está disponível no GitHub, organizado em fases conforme
        documentado no roadmap do projeto.
        
        ---
        
        ⚕️ **Aviso Legal**: Este sistema é uma ferramenta de apoio à decisão e não
        substitui a avaliação de um profissional de saúde qualificado.
        """
    )


def main():
    """Função principal da aplicação."""
    # Sidebar com navegação
    st.sidebar.title("🏥 Sistema de Diagnóstico")
    st.sidebar.markdown("---")

    pagina = st.sidebar.radio(
        "Navegação",
        ["🩺 Sistema Preditivo", "📈 Dashboard Analítico", "ℹ️ Sobre"],
        label_visibility="collapsed",
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown(
        """
        **Tech Challenge 4**  
        FIAP/POSTECH  
        Data Analytics
        """
    )

    # Roteamento de páginas
    if pagina == "🩺 Sistema Preditivo":
        pagina_predicao()
    elif pagina == "📈 Dashboard Analítico":
        pagina_dashboard()
    else:
        pagina_sobre()


if __name__ == "__main__":
    main()
