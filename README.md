# Laboratório de Experimentação de Software 4  
## Visualização de Dados com Business Intelligence (BI)

### Integrantes
- **Gustavo Barbosa**
- **Gabriel Silva**

---

## Objetivo Geral
Este laboratório tem como objetivo aplicar técnicas de **Business Intelligence (BI)** para explorar, analisar e visualizar dados provenientes de experimentos realizados nos laboratórios anteriores, com foco na criação de dashboards interativos utilizando ferramentas de BI (Power BI, Tableau ou Google Data Studio).

O objetivo é transformar os dados coletados em informações visuais que auxiliem na **tomada de decisão** e **interpretação dos resultados** das questões de pesquisa.

---

## Lab04S01 — Caracterização do Dataset

Nesta primeira etapa, foi realizada a **exploração inicial e caracterização do dataset** `pull_requests.csv`. Essa fase teve como objetivo compreender o comportamento geral das variáveis analisadas.

### **Entregas principais**
- Importação do dataset no Power BI  
- Construção de gráficos exploratórios, incluindo:
  - Distribuição do tempo de análise dos PRs (`AnalysisTimeHours`)
  - Distribuição do tamanho dos PRs (`Additions` + `Deletions`)
  - Distribuição das revisões (`Reviews`)
  - Distribuição das interações (`Comments`, `Participants`, `Reviews`)
- Inclusão de textos explicativos e títulos descritivos no dashboard

Essa caracterização fornece uma visão geral do conjunto de dados, servindo de base para análises mais detalhadas nas etapas seguintes.

---

Lab04S02 — Visualizações das RQs 1 e 2

Nesta sprint, foram construídas visualizações específicas para as duas primeiras questões de pesquisa:

### **RQ1**  
**Qual a relação entre o tamanho dos PRs e o feedback final das revisões (merged ou closed)?**

### **RQ2**  
**Qual a relação entre o tempo de análise dos PRs e o feedback final das revisões?**

As visualizações foram elaboradas em Power BI e permitem:

- Comparação direta entre PRs aprovados (merged) e rejeitados (closed)  
- Observação de tendências  
- Identificação de padrões relevantes no comportamento dos PRs  

Essas visualizações complementam os achados estatísticos do Laboratório 3, agora apresentados em formato visual com técnicas de BI.

---

Lab04S03 — Dashboard Final e Consolidação das RQs

Na última sprint, o objetivo é consolidar **todo o dashboard final**, reunindo:

- A caracterização do dataset  
- As visualizações das RQs 1 e 2  
- As visualizações das demais RQs (3–8) em formato de dashboard

---

## Ferramentas Utilizadas
- **Python (Pandas / Seaborn / Matplotlib)** – para pré-processamento e exploração inicial.  
- **Power BI** – para construção do dashboard interativo e visualização final dos dados.  


