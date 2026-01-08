# Sistema de Diagnóstico Preditivo de Obesidade

> **Tech Challenge Fase 4 - FIAP/POSTECH Data Analytics**

Sistema de Machine Learning para apoio à decisão médica no diagnóstico de níveis de obesidade, considerando fatores genéticos, comportamentais e ambientais.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3+-orange.svg)
![Accuracy](https://img.shields.io/badge/Accuracy-99.04%25-brightgreen.svg)

---

## Acesse a Aplicação

A aplicação está disponível online na Streamlit Cloud:

**[Acessar Sistema de Diagnóstico](https://sdo-techc4-arnaldo.streamlit.app/)**

---

## Sobre o Projeto

O sistema utiliza um modelo de **Random Forest Classifier** treinado com dados de hábitos alimentares, estilo de vida e características físicas para prever o nível de obesidade de pacientes em 7 categorias:

| Categoria | Descrição |
|-----------|-----------|
| Insufficient_Weight | Peso insuficiente |
| Normal_Weight | Peso normal |
| Overweight_Level_I | Sobrepeso nível I |
| Overweight_Level_II | Sobrepeso nível II |
| Obesity_Type_I | Obesidade tipo I |
| Obesity_Type_II | Obesidade tipo II |
| Obesity_Type_III | Obesidade tipo III (mórbida) |

---

## Funcionalidades

### Sistema Preditivo
- Formulário intuitivo para inserção de dados do paciente
- Predição instantânea do nível de obesidade
- Recomendações clínicas personalizadas

### Dashboard Analítico
- Visualizações interativas com Plotly
- Análise de fatores de risco por nível de obesidade
- Matriz de correlação entre variáveis
- Explorador de dados 3D com filtros dinâmicos

### Sobre
- Metodologia utilizada
- Métricas de performance do modelo

---

## Métricas do Modelo

| Métrica | Valor |
|---------|-------|
| **Acurácia (CV 5-fold)** | 98.86% |
| **Acurácia (Teste)** | 99.04% |
| Precision Média | 0.99 |
| Recall Médio | 0.99 |
| F1-Score Médio | 0.99 |

---

## Executar Localmente

### Pré-requisitos
- Python 3.10 ou superior

### Instalação

```bash
# Clone o repositório
git clone https://github.com/suprarn/tech-challenge-4.git
cd tech-challenge-4

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
streamlit run app.py
```

Acesse: http://localhost:8501

---

## Estrutura do Repositório

```
tech-challenge-4/
├── data/
│   ├── Obesity.csv              # Dataset original
│   └── dicionario.txt           # Descrição das variáveis
├── scripts/
│   ├── 1_eda.ipynb              # Análise Exploratória (FASE 1)
│   ├── 2_preprocessing.py       # Pipeline de Features (FASE 2)
│   └── 3_training.py            # Treinamento do Modelo (FASE 3)
├── plots/                       # Visualizações geradas no EDA
├── app.py                       # Aplicação Streamlit
├── modelo.joblib                # Modelo serializado (joblib)
├── label_encoder.joblib         # Encoder do target (joblib)
├── requirements.txt             # Dependências Python
└── README.md
```

---

## Stack Tecnológica

- **Linguagem**: Python 3.10+
- **Machine Learning**: Scikit-learn (RandomForestClassifier)
- **Visualização**: Plotly, Matplotlib, Seaborn
- **Interface**: Streamlit
- **Dados**: Pandas, NumPy

---

## Aviso Legal

Este sistema é uma ferramenta **meramente informativa** e não substitui a avaliação de um profissional de saúde qualificado. O diagnóstico final deve ser sempre realizado por um médico.

---

## Licença

Projeto desenvolvido para fins acadêmicos - Tech Challenge Fase 4, FIAP/POSTECH Data Analytics.

**Autor:** Arnaldo Janssen Tavares Toledo Laudares
