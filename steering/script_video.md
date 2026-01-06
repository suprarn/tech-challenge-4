# ROTEIRO DO VÍDEO DE APRESENTAÇÃO

> **Duração alvo**: 7-10 minutos
> **Formato**: Slides com narração + Demonstração ao vivo da aplicação

---

## SLIDE 1: ABERTURA (30 segundos)

### Texto do Slide:
```
SISTEMA DE DIAGNÓSTICO PREDITIVO DE OBESIDADE
Aplicação de Machine Learning para Apoio à Decisão Médica

Tech Challenge Fase 4
FIAP/POSTECH - Data Analytics

Arnaldo Janssen Tavares Toledo Laudares
```

### Fala:
"Olá! Sou Arnaldo Laudares e hoje vou apresentar o Sistema de Diagnóstico Preditivo de Obesidade, desenvolvido como parte do Tech Challenge Fase 4 da FIAP POSTECH.

O objetivo deste projeto é criar uma ferramenta de apoio à decisão médica que auxilie profissionais de saúde no diagnóstico de níveis de obesidade, utilizando técnicas avançadas de Machine Learning."

---

## SLIDE 2: O PROBLEMA (1 minuto)

### Texto do Slide:
```
A OBESIDADE COMO PROBLEMA DE SAÚDE PÚBLICA

Condição médica multifatorial caracterizada por:
• Fatores GENÉTICOS: histórico familiar, predisposição metabólica
• Fatores COMPORTAMENTAIS: alimentação, sedentarismo, tabagismo
• Fatores AMBIENTAIS: acesso a alimentos, meio de transporte

Impactos clínicos:
• Doenças cardiovasculares  • Diabetes Tipo 2
• Hipertensão arterial      • Apneia do sono
• Problemas articulares     • Maior risco oncológico

DESAFIO: Classificar pacientes em 7 níveis de obesidade
para intervenção médica personalizada
```

### Fala:
"A obesidade é uma condição médica multifatorial que afeta milhões de pessoas no mundo. Ela está associada a três grandes grupos de fatores: genéticos, como o histórico familiar; comportamentais, como hábitos alimentares e sedentarismo; e ambientais, como o meio de transporte utilizado.

As consequências clínicas são severas: doenças cardiovasculares, diabetes tipo 2, hipertensão, apneia do sono e até maior risco de alguns tipos de câncer.

O desafio proposto foi desenvolver um modelo de Machine Learning capaz de classificar pacientes em 7 níveis distintos de obesidade, permitindo que a equipe médica direcione intervenções personalizadas para cada perfil."

---

## SLIDE 3: O DATASET (1 minuto)

### Texto do Slide:
```
DATASET: Obesity.csv

Registros: 2.111 (após remoção de 24 duplicatas: 2.087)
Variáveis: 17 features + 1 target

┌─────────────────────────────────────────────────────────────┐
│ VARIÁVEIS DEMOGRÁFICAS                                      │
│ Gender, Age, Height, Weight                                 │
├─────────────────────────────────────────────────────────────┤
│ HÁBITOS ALIMENTARES                                         │
│ FAVC (alimentos calóricos), FCVC (vegetais), NCP (refeições)│
│ CAEC (petiscos), CALC (álcool), CH2O (água)                 │
├─────────────────────────────────────────────────────────────┤
│ ESTILO DE VIDA                                              │
│ SMOKE (tabagismo), FAF (atividade física), TUE (eletrônicos)│
│ MTRANS (transporte), SCC (monitoramento calórico)           │
├─────────────────────────────────────────────────────────────┤
│ FATOR GENÉTICO                                              │
│ family_history (histórico familiar de sobrepeso)            │
└─────────────────────────────────────────────────────────────┘

TARGET: Obesity (7 classes)
Insufficient_Weight | Normal_Weight | Overweight I/II | Obesity I/II/III
```

### Fala:
"O dataset utilizado contém 2.111 registros com 17 variáveis. Após a remoção de 24 linhas duplicadas, trabalhamos com 2.087 observações.

As variáveis se dividem em quatro grupos: demográficas como idade, peso e altura; hábitos alimentares como consumo de alimentos calóricos, vegetais e água; estilo de vida incluindo atividade física, tabagismo e tempo em dispositivos eletrônicos; e o fator genético representado pelo histórico familiar de sobrepeso.

A variável alvo possui 7 classes distintas, desde peso insuficiente até obesidade tipo III, também conhecida como obesidade mórbida."

---

## SLIDE 4: ANÁLISE EXPLORATÓRIA - EDA (1.5 minutos)

### Texto do Slide:
```
FASE 1: ANÁLISE EXPLORATÓRIA DE DADOS (EDA)

Qualidade dos Dados:
✓ Zero valores nulos em todas as 17 colunas
✓ 24 duplicatas removidas (1.1% dos dados)
✓ Distribuição balanceada do target (~14% por classe)

Principais Descobertas:
┌──────────────────────────────────────────────────────┐
│ 82% dos pacientes têm HISTÓRICO FAMILIAR de obesity  │
│ 89% consomem ALIMENTOS ALTAMENTE CALÓRICOS          │
│ 75% utilizam TRANSPORTE PÚBLICO (sedentarismo)      │
│ FAF médio = 1.0 (baixa atividade física semanal)    │
│ CH2O médio = 2.0 (consumo de água moderado)         │
└──────────────────────────────────────────────────────┘

Feature Engineering:
• Criação do BMI (Índice de Massa Corporal)
  BMI = Weight / Height²
• Forte correlação BMI × Weight (r = 0.87)

36 visualizações geradas (univariadas, bivariadas, correlação)
```

### Fala:
"Na Fase 1, realizamos uma análise exploratória completa. A boa notícia é que o dataset está limpo: zero valores nulos e apenas 24 duplicatas que foram removidas. A distribuição do target é relativamente balanceada, com aproximadamente 14% em cada classe.

Os insights mais relevantes: 82% dos pacientes possuem histórico familiar de obesidade, confirmando o peso do fator genético; 89% consomem alimentos altamente calóricos; e 75% utilizam transporte público, o que pode indicar menor atividade física.

Como feature engineering, criamos o BMI - Índice de Massa Corporal - calculado como peso dividido pela altura ao quadrado. Esta feature apresentou correlação de 0.87 com o peso, sendo um preditor importante.

Geramos 36 visualizações entre análises univariadas, bivariadas e matriz de correlação."

---

## SLIDE 5: PIPELINE DE PRÉ-PROCESSAMENTO (1 minuto)

### Texto do Slide:
```
FASE 2: FEATURE ENGINEERING E PRÉ-PROCESSAMENTO

Pipeline de Transformação (sklearn ColumnTransformer):

┌─────────────────────────────────────────────────────────────┐
│ VARIÁVEIS NUMÉRICAS (9 features)                            │
│ Age, Height, Weight, BMI, FCVC, NCP, CH2O, FAF, TUE         │
│ ──────────────────────────────────────────────────────────  │
│ Transformação: StandardScaler (μ=0, σ=1)                    │
├─────────────────────────────────────────────────────────────┤
│ VARIÁVEIS ORDINAIS (2 features)                             │
│ CAEC, CALC                                                  │
│ ──────────────────────────────────────────────────────────  │
│ Transformação: OrdinalEncoder                               │
│ Ordem: no → Sometimes → Frequently → Always (0-3)           │
├─────────────────────────────────────────────────────────────┤
│ VARIÁVEIS CATEGÓRICAS NOMINAIS (6 features)                 │
│ Gender, family_history, FAVC, SMOKE, SCC, MTRANS            │
│ ──────────────────────────────────────────────────────────  │
│ Transformação: OneHotEncoder (drop='first')                 │
└─────────────────────────────────────────────────────────────┘

Output: 20 features após transformação
```

### Fala:
"Na Fase 2, implementamos o pipeline de pré-processamento usando ColumnTransformer do scikit-learn.

Para as 9 variáveis numéricas, aplicamos StandardScaler, normalizando os dados para média zero e desvio padrão um.

As variáveis CAEC e CALC, que representam consumo entre refeições e consumo de álcool, são ordinais. Elas seguem uma ordem natural de frequência, então utilizamos OrdinalEncoder mapeando de 'no' até 'Always' em uma escala de 0 a 3.

Para as 6 variáveis categóricas nominais como gênero, histórico familiar e meio de transporte, aplicamos OneHotEncoder com drop first para evitar multicolinearidade.

Ao final, o dataset transformado possui 20 features prontas para modelagem."

---

## SLIDE 6: MODELAGEM E RESULTADOS (1.5 minutos)

### Texto do Slide:
```
FASE 3: MODELAGEM E VALIDAÇÃO

Algoritmo: RandomForestClassifier
┌────────────────────────────────────────┐
│ Hiperparâmetros:                       │
│ • n_estimators = 200 árvores           │
│ • max_depth = 20                       │
│ • min_samples_split = 5                │
│ • min_samples_leaf = 2                 │
│ • class_weight = 'balanced'            │
│ • random_state = 42                    │
└────────────────────────────────────────┘

Validação: Stratified 5-Fold Cross-Validation
Split: 80% treino (1.669) / 20% teste (418)

┌──────────────────────────────────────────────────────────┐
│                    MÉTRICAS FINAIS                       │
├──────────────────────────────────────────────────────────┤
│ Acurácia Cross-Validation:  98.86% (±0.80%)              │
│ Acurácia no Teste:          99.04%                       │
│ Precision Média:            0.99                         │
│ Recall Médio:               0.99                         │
│ F1-Score Médio:             0.99                         │
├──────────────────────────────────────────────────────────┤
│ META DO PROJETO: 75%    ✓ SUPERADA EM 24 p.p.            │
└──────────────────────────────────────────────────────────┘
```

### Fala:
"Na Fase 3, optamos pelo Random Forest Classifier, um algoritmo de ensemble que combina múltiplas árvores de decisão. Configuramos 200 árvores com profundidade máxima de 20 e class weight balanceado para lidar com eventuais desbalanceamentos.

Para validação, utilizamos Stratified K-Fold com 5 folds, garantindo que cada fold mantivesse a proporção original das classes. O split foi 80/20, resultando em 1.669 amostras para treino e 418 para teste.

Os resultados superaram significativamente a meta de 75%. Na validação cruzada, atingimos 98.86% de acurácia com desvio de apenas 0.80%. No conjunto de teste, a acurácia foi de 99.04%.

Precision, Recall e F1-Score ficaram todos em 0.99, indicando que o modelo tem excelente capacidade de classificação para todas as 7 classes. Superamos a meta do projeto em 24 pontos percentuais."

---

## SLIDE 7: ARQUITETURA DA APLICAÇÃO (30 segundos)

### Texto do Slide:
```
APLICAÇÃO STREAMLIT

Arquitetura:
┌─────────────────────────────────────────────────────────┐
│                    FRONTEND (Streamlit)                 │
├──────────────────┬──────────────────┬───────────────────┤
│ Sistema Preditivo│ Dashboard        │ Sobre             │
│ (Formulário)     │ (Visualizações)  │ (Documentação)    │
└────────┬─────────┴────────┬─────────┴─────────┬─────────┘
         │                  │                   │
         ▼                  ▼                   ▼
┌─────────────────────────────────────────────────────────┐
│                   BACKEND (Python)                      │
│  modelo.pkl + label_encoder.pkl + Obesity.csv           │
└─────────────────────────────────────────────────────────┘

Stack: Python 3.10+ | Streamlit | Scikit-learn | Plotly
```

### Fala:
"A aplicação foi desenvolvida em Streamlit e possui três páginas principais: o Sistema Preditivo com formulário de entrada; o Dashboard Analítico com visualizações interativas em Plotly; e a página Sobre com documentação técnica.

O backend carrega o modelo serializado e o encoder de labels, permitindo predições em tempo real."

---

## DEMONSTRAÇÃO AO VIVO (2-3 minutos)

### Instruções:
```
[COMPARTILHAR TELA - Abrir http://localhost:8501]

ROTEIRO DA DEMONSTRAÇÃO:

1. SISTEMA PREDITIVO (1.5 min)
   - Preencher formulário com dados fictícios de um paciente
   - Exemplo 1: Paciente saudável (Height=1.75, Weight=70, FAF=3)
   - Mostrar resultado: "Peso Normal" + recomendações
   - Exemplo 2: Paciente de risco (Weight=120, FAF=0, family_history=yes)
   - Mostrar resultado: "Obesidade Tipo II" + recomendações

2. DASHBOARD ANALÍTICO (1 min)
   - Tab "Distribuição do Target": mostrar gráfico de barras interativo
   - Tab "Análise Bivariada": selecionar BMI, mostrar boxplot
   - Tab "Correlações": mostrar heatmap e scatter plot
   - Tab "Explorador de Dados": aplicar filtros, mostrar gráfico 3D

3. SOBRE (30 seg)
   - Mostrar metodologia documentada
   - Destacar métricas finais
```

### Fala durante demonstração:
"Vamos agora para a demonstração ao vivo. Aqui temos o Sistema Preditivo. Vou inserir dados de um paciente hipotético...

[Preencher formulário]

Ao clicar em Realizar Diagnóstico, o modelo processa os dados e retorna o nível de obesidade predito, junto com uma descrição clínica e recomendações específicas.

[Mostrar Dashboard]

No Dashboard Analítico, temos gráficos interativos. Posso explorar a distribuição do target, analisar como cada variável se relaciona com os níveis de obesidade, visualizar a matriz de correlação, e até explorar os dados em uma visualização 3D com filtros dinâmicos.

Todos esses gráficos são interativos - posso passar o mouse para ver detalhes, dar zoom, e filtrar os dados."

---

## SLIDE 8: CONCLUSÃO E INSIGHTS DE NEGÓCIO (1.5 minutos)

### Texto do Slide:
```
CONCLUSÃO: VALOR ENTREGUE PARA A EQUIPE MÉDICA

┌─────────────────────────────────────────────────────────────────┐
│                 INSIGHTS DE NEGÓCIO OBTIDOS                     │
├─────────────────────────────────────────────────────────────────┤
│ 1. FATOR GENÉTICO É DETERMINANTE                                │
│    82% dos pacientes obesos têm histórico familiar              │
│    → Triagem prioritária para pacientes com esse perfil         │
│                                                                 │
│ 2. ESTILO DE VIDA SEDENTÁRIO                                    │
│    75% usam transporte público + baixa atividade física (FAF=1) │
│    → Programas de incentivo à mobilidade ativa                  │
│                                                                 │
│ 3. HÁBITOS ALIMENTARES DE RISCO                                 │
│    89% consomem alimentos altamente calóricos regularmente      │
│    → Campanhas de reeducação alimentar direcionadas             │
│                                                                 │
│ 4. BMI COMO INDICADOR CHAVE                                     │
│    Forte preditor (correlação 0.87 com peso)                    │
│    → Monitoramento contínuo do IMC em consultas de rotina       │
└─────────────────────────────────────────────────────────────────┘

APLICAÇÃO PRÁTICA:
Sistema disponível para triagem rápida em unidades de saúde,
permitindo classificação imediata e encaminhamento adequado.
```

### Fala:
"Chegamos à conclusão do projeto, e gostaria de destacar os principais insights de negócio que extraímos dessa análise.

Primeiro, confirmamos que o fator genético é determinante: 82% dos pacientes com obesidade possuem histórico familiar. Isso sugere que a triagem deve ser prioritária para pacientes com esse perfil, permitindo intervenções preventivas mais cedo.

Segundo, identificamos um padrão de estilo de vida sedentário: 75% utilizam transporte público e a média de atividade física semanal é baixa. Isso abre espaço para programas de incentivo à mobilidade ativa, como caminhadas ou uso de bicicleta.

Terceiro, os hábitos alimentares são preocupantes: 89% consomem alimentos altamente calóricos com frequência. Campanhas de reeducação alimentar direcionadas a esse público podem ter grande impacto.

Por fim, o BMI se mostrou um indicador-chave com alta correlação com o peso, reforçando a importância do monitoramento contínuo do IMC em consultas de rotina.

Na prática, este sistema pode ser utilizado para triagem rápida em unidades de saúde, permitindo classificação imediata do paciente e encaminhamento adequado conforme o nível de risco identificado."

---

## SLIDE 9: ENTREGÁVEIS E ENCERRAMENTO (30 segundos)

### Texto do Slide:
```
ENTREGÁVEIS DO PROJETO

✓ Pipeline de ML documentado (EDA → Preprocessing → Training)
✓ Modelo RandomForest com 99.04% de acurácia
✓ Aplicação Streamlit com sistema preditivo + dashboard
✓ Repositório GitHub organizado e documentado

┌─────────────────────────────────────────────────────────────────┐
│                      PRÓXIMOS PASSOS                            │
├─────────────────────────────────────────────────────────────────┤
│ • Validação clínica com dados reais de pacientes                │
│ • Integração com sistemas hospitalares (HL7/FHIR)               │
│ • Expansão para outros indicadores de saúde                     │
└─────────────────────────────────────────────────────────────────┘

                         OBRIGADO!
                    Arnaldo Laudares
              FIAP/POSTECH - Data Analytics
```

### Fala:
"Para finalizar, entregamos todos os requisitos do projeto: um pipeline de Machine Learning completo e documentado, um modelo com 99% de acurácia - superando em muito a meta de 75% -, uma aplicação Streamlit funcional com sistema preditivo e dashboard interativo, e um repositório GitHub organizado.

Como próximos passos, este sistema poderia ser validado clinicamente com dados reais de pacientes, integrado a sistemas hospitalares utilizando padrões como HL7 ou FHIR, e expandido para outros indicadores de saúde.

Agradeço a atenção de todos. Os links da aplicação, repositório e vídeo estão disponíveis no arquivo de entrega. Muito obrigado!"

---

## NOTAS DE PRODUÇÃO

### Configurações de Gravação:
- Software: OBS Studio ou similar
- Resolução: 1920x1080 (Full HD)
- Duração: 7-10 minutos
- Formato: MP4

### Checklist Pré-Gravação:
- [ ] Aplicação Streamlit rodando em localhost:8501
- [ ] Slides abertos em modo apresentação
- [ ] Browser com zoom adequado para captura
- [ ] Microfone testado e funcionando
- [ ] Notificações do sistema desativadas

### Durante a Gravação:
- Falar pausadamente e com clareza
- Mover o mouse de forma suave
- Pausar brevemente entre slides para transições
- Na demonstração, explicar enquanto interage

### Pós-Gravação:
- Verificar se áudio e vídeo estão sincronizados
- Cortar silêncios longos ou erros
- Adicionar transições suaves entre seções
