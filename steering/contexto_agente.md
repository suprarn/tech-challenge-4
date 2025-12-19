# BANCO DE CONTEXTO DO AGENTE

> **Última atualização**: 2025-12-19 12:45
> **Fase atual**: ✅ PROJETO CONCLUÍDO 

---

## 1. VISÃO GERAL DO PROJETO

**Objetivo**: Desenvolver um modelo de Machine Learning para auxílio ao diagnóstico de obesidade em ambiente hospitalar, com deploy via Streamlit e dashboard analítico.

**Entregáveis Obrigatórios**:
1. Pipeline de ML com feature engineering e treinamento
2. Modelo com acurácia > 75%
3. Aplicação preditiva Streamlit
4. Dashboard analítico com insights para equipe médica
5. Repositório GitHub organizado por fases
6. Vídeo de apresentação (4-10 min)

---

## 2. DIAGNÓSTICO DO ESTADO ATUAL

### ✅ FASE 1 - EDA (CONCLUÍDA)
- **Arquivo**: `scripts/1_eda.ipynb`
- **Outputs**: 36 gráficos em `plots/`
- **Insights documentados**:
  - 2111 registros, 17 colunas, sem valores nulos
  - 24 duplicatas identificadas (a remover)
  - 82% com histórico familiar de obesidade
  - Perfil: jovens adultos (~24 anos), peso médio 86.6 kg
  - FAF baixo (~1), consumo de água ~2 copos/dia

### ✅ FASE 2 - PREPROCESSING (CONCLUÍDA)
- **Arquivo**: `scripts/2_preprocessing.py`
- **Implementações**:
  - `carregar_dados()`: limpeza e remoção de duplicatas
  - `criar_bmi()`: feature engineering (IMC)
  - `obter_preprocessor()`: ColumnTransformer com:
    - StandardScaler para numéricas
    - OrdinalEncoder para CAEC/CALC
    - OneHotEncoder para categóricas nominais
  - `obter_target_encoder()`: LabelEncoder para variável alvo

### ✅ FASE 3 - MODELAGEM (CONCLUÍDA)
- **Script**: `scripts/3_training.py`
- **Modelo**: RandomForestClassifier (200 árvores, max_depth=20)
- **Métricas**:
  - Acurácia CV (5-fold): 98.86% (+/- 0.80%)
  - **Acurácia no teste: 99.04%** ✅
  - Precision/Recall/F1: ~0.99 para todas as classes
- **Artefatos**: `modelo.pkl`, `label_encoder.pkl` salvos

### 🔲 FASE 4 - SISTEMA PREDITIVO (NÃO INICIADA)
- **Arquivo vazio**: `app.py`
- **Requisitos**:
  - Interface Streamlit com input de dados do paciente
  - Predição do nível de obesidade
  - Dashboard com insights analíticos
  - Visão de negócio para equipe médica

### 🔲 FASE 5 - ENTREGA (NÃO INICIADA)
- **Pendentes**: README.md, requirements.txt, script de vídeo

---

## 3. PRÓXIMAS AÇÕES

### TAREFA IMEDIATA: Completar FASE 3
1. Criar `scripts/3_training.py` com:
   - Carregamento de dados via `2_preprocessing.py`
   - Split treino/teste estratificado
   - Treinamento com validação cruzada
   - Métricas: accuracy, precision, recall, F1, confusion matrix
   - Serialização do modelo e encoder

### SEQUÊNCIA PLANEJADA:
1. [EM ANDAMENTO] Validar/recriar pipeline de treinamento
2. [PRÓXIMO] Desenvolver `app.py` com Streamlit
3. [PRÓXIMO] Implementar dashboard analítico
4. [FUTURO] Documentação e preparação para entrega

---

## 4. DECISÕES TÉCNICAS

### Modelo de ML
- **Candidatos a avaliar**: Random Forest, Gradient Boosting, XGBoost
- **Métrica principal**: Acurácia (meta > 75%)
- **Validação**: Stratified K-Fold (5 folds)

### Arquitetura Streamlit
- **Páginas planejadas**:
  1. Sistema Preditivo (input → predição)
  2. Dashboard Analítico (gráficos + insights)
  3. Sobre o Projeto (explicação do modelo)

---

## 5. LOG DE ATIVIDADES

| Data | Ação | Resultado |
|------|------|-----------|
| 2025-12-19 12:10 | Análise inicial dos documentos steering | Diagnóstico completo do projeto |
| 2025-12-19 12:10 | Criação do documento de contexto | Este arquivo |

---

## 6. NOTAS PARA CONTINUIDADE

Se a janela de contexto for reiniciada:
1. Ler este documento primeiro
2. Verificar arquivos em `scripts/` para status atual
3. Continuar da "TAREFA IMEDIATA" listada acima
