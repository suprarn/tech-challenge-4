# ROTEIRO DO VÍDEO DE APRESENTAÇÃO

> **Duração alvo**: 5-7 minutos
> **Formato**: Apresentação + Demonstração ao vivo

---

## ABERTURA (30 segundos)

**[Slide: Título do Projeto]**

"Olá! Hoje vou apresentar o Sistema de Diagnóstico Preditivo de Obesidade, desenvolvido como parte do Tech Challenge Fase 4 da FIAP POSTECH.

O objetivo deste projeto é criar uma ferramenta de apoio à decisão médica que auxilie profissionais de saúde no diagnóstico de níveis de obesidade, utilizando técnicas de Machine Learning."

---

## CONTEXTO DO PROBLEMA (1 minuto)

**[Slide: O Problema]**

"A obesidade é uma condição médica multifatorial que afeta milhões de pessoas no mundo. Ela está associada a fatores genéticos, comportamentais e ambientais.

Para este desafio, recebemos um dataset com 2.111 registros contendo 17 variáveis sobre hábitos alimentares, estilo de vida e características físicas dos pacientes.

Nosso objetivo era desenvolver um modelo com mais de 75% de acurácia e criar uma aplicação para auxiliar a equipe médica."

---

## METODOLOGIA (1.5 minutos)

**[Slide: Pipeline de ML]**

"O projeto foi dividido em 5 fases:

**FASE 1 - Análise Exploratória**: Realizamos análise univariada e bivariada de todas as variáveis, gerando mais de 30 visualizações. Identificamos que 82% dos pacientes têm histórico familiar de obesidade.

**FASE 2 - Feature Engineering**: Implementamos um pipeline robusto com:
- StandardScaler para variáveis numéricas
- OrdinalEncoder para variáveis ordinais como consumo de álcool
- OneHotEncoder para variáveis categóricas
- E criamos a feature BMI (Índice de Massa Corporal)

**FASE 3 - Modelagem**: Treinamos um Random Forest Classifier com 200 árvores, utilizando validação cruzada estratificada de 5 folds."

---

## RESULTADOS (1 minuto)

**[Slide: Métricas]**

"Os resultados superaram significativamente a meta de 75%:

- Acurácia na validação cruzada: 98.86%
- Acurácia no conjunto de teste: 99.04%
- Precision e Recall médios de 0.99 para todas as 7 classes

O modelo consegue distinguir com alta precisão entre peso insuficiente, peso normal, sobrepeso níveis I e II, e obesidade tipos I, II e III."

---

## DEMONSTRAÇÃO DA APLICAÇÃO (2-3 minutos)

**[Compartilhar tela com Streamlit]**

"Agora vou demonstrar a aplicação desenvolvida em Streamlit.

**Sistema Preditivo**: Aqui temos o formulário onde o médico insere os dados do paciente - idade, peso, altura, hábitos alimentares e estilo de vida. Ao clicar em 'Realizar Diagnóstico', o sistema retorna o nível de obesidade predito junto com recomendações clínicas específicas.

**Dashboard Analítico**: Esta página apresenta visualizações interativas dos dados, permitindo que a equipe médica explore os fatores de risco. Podemos ver a distribuição da população por nível de obesidade e analisar correlações entre as variáveis.

**Sobre o Projeto**: Aqui documentamos toda a metodologia e métricas para transparência técnica."

---

## CONCLUSÃO (30 segundos)

**[Slide: Entregáveis]**

"Para resumir, entregamos:
- Pipeline completo de Machine Learning documentado
- Modelo com 99% de acurácia
- Aplicação Streamlit funcional
- Dashboard analítico com insights
- Repositório GitHub organizado por fases

Obrigado pela atenção! O link da aplicação e do repositório estão disponíveis no arquivo de entrega."

---

## NOTAS TÉCNICAS

- Gravar usando OBS ou ferramenta similar
- Manter o vídeo entre 4-7 minutos
- Focar na visão de negócio e valor para a equipe médica
- Demonstrar pelo menos 2 predições na aplicação
- Mostrar a responsividade do dashboard
