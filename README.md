# 🏥 Sistema de Diagnóstico Preditivo de Obesidade

> **Tech Challenge Fase 4 - FIAP/POSTECH Data Analytics**

Sistema de Machine Learning para apoio à decisão médica no diagnóstico de níveis de obesidade, considerando fatores genéticos, comportamentais e ambientais.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3+-orange.svg)
![Accuracy](https://img.shields.io/badge/Accuracy-99.04%25-brightgreen.svg)

---

## 📋 Sobre o Projeto

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

## 🚀 Como Executar

### Pré-requisitos
- Python 3.10 ou superior
- pip

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/tech-challenge-4.git
cd tech-challenge-4

# Instale as dependências
pip install -r requirements.txt
```

### Executando a Aplicação

```bash
streamlit run app.py
```

Acesse: http://localhost:8501

---

## 📁 Estrutura do Projeto

```
tech-challenge-4/
├── 📂 data/
│   ├── Obesity.csv              # Dataset original
│   └── dicionario.txt           # Descrição das variáveis
├── 📂 scripts/
│   ├── 1_eda.ipynb              # Análise Exploratória (FASE 1)
│   ├── 2_preprocessing.py       # Pipeline de Features (FASE 2)
│   └── 3_training.py            # Treinamento do Modelo (FASE 3)
├── 📂 plots/                     # Visualizações do EDA
├── 📂 steering/                  # Documentos de direção do projeto
├── app.py                        # Aplicação Streamlit (FASE 4)
├── modelo.pkl                    # Modelo serializado
├── label_encoder.pkl             # Encoder do target
├── requirements.txt              # Dependências
└── README.md                     # Este arquivo
```

---

## 📊 Métricas do Modelo

| Métrica | Valor |
|---------|-------|
| **Acurácia (CV 5-fold)** | 98.86% |
| **Acurácia (Teste)** | 99.04% |
| Precision Média | 0.99 |
| Recall Médio | 0.99 |
| F1-Score Médio | 0.99 |

---

## 🛠️ Stack Tecnológica

- **Linguagem**: Python 3.10+
- **Machine Learning**: Scikit-learn
- **Visualização**: Matplotlib, Seaborn
- **Interface**: Streamlit
- **Dados**: Pandas, NumPy

---

## 📱 Funcionalidades da Aplicação

### 🩺 Sistema Preditivo
- Formulário intuitivo para inserção de dados do paciente
- Predição instantânea do nível de obesidade
- Recomendações clínicas personalizadas

### 📈 Dashboard Analítico
- Visualizações interativas dos dados
- Análise de fatores de risco
- Matriz de correlação entre variáveis

### ℹ️ Sobre
- Metodologia utilizada
- Métricas de performance
- Informações técnicas

---

## 👥 Equipe

Tech Challenge Fase 4 - FIAP/POSTECH Data Analytics

---

## ⚠️ Aviso Legal

Este sistema é uma ferramenta de **apoio à decisão** e não substitui a avaliação de um profissional de saúde qualificado. O diagnóstico final deve ser sempre realizado por um médico.

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos como parte do Tech Challenge da FIAP/POSTECH.
