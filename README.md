# Previsão de Churn em Telecomunicações 📉

Este projeto tem caráter educacional e demonstrativo.


## 📌 Problema de Negócio
A perda de clientes (Churn) é um dos maiores drenos de receita em empresas de telecom. O objetivo deste projeto é desenvolver um modelo de Machine Learning capaz de identificar clientes com alta probabilidade de cancelamento, permitindo que a empresa aja preventivamente.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python
- **Bibliotecas:** Scikit-Learn, Pandas, Numpy, Seaborn, Matplotlib.
- **Técnicas:** Pipeline de Dados, Tratamento de Classes Desbalanceadas, GridSearch, Cross-Validation.

## 📊 Metodologia
1. **Limpeza de Dados:** Tratamento de valores nulos e conversão de tipos (ex: `TotalCharges`).
2. **EDA (Análise Exploratória):** Identificação de perfis de risco (Contratos mensais e fibras ópticas mostraram maior churn).
3. **Pré-processamento:** OneHotEncoding para variáveis categóricas e Scaling para numéricas.
4. **Modelagem:** Comparação entre *Logistic Regression* e *Random Forest*.
5. **Otimização:** Tuning de hiperparâmetros com GridSearchCV focado na métrica **Recall**.

## 🚀 Resultados
O modelo final (**Random Forest Otimizado**) superou significativamente o baseline, priorizando a identificação de cancelamentos reais.

| Métrica (Classe Churn) | Modelo Inicial | Modelo Otimizado | Impacto |
| :--- | :--- | :--- | :--- |
| **Recall (Captura)** | 51% | **~80%** | +29% de clientes em risco identificados |
| **Precisão** | 62% | 47% | Trade-off aceito para maximizar retenção |

*O modelo otimizado conseguiu identificar cerca de 80% de todos os clientes que cancelaram, reduzindo drasticamente os "Falsos Negativos" (clientes que saem sem ser notados).*

## 💼 Impacto de Negócio
Com o modelo implantado, a empresa pode focar seus esforços de retenção (descontos, contatos proativos) nos 30-40% da base apontados como risco, em vez de gastar recursos aleatoriamente. Assumindo que reter um cliente é 5x mais barato que adquirir um novo, o aumento do Recall para 80% gera proteção direta de receita.