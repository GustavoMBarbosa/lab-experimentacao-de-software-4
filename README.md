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

## Sprint Atual — Lab04S01: Caracterização do Dataset
Nesta primeira sprint, o foco é na **caracterização do dataset** utilizado no trabalho.  
Foram utilizadas as bases geradas no **Laboratório 3**, compostas por informações de *Pull Requests (PRs)* de repositórios populares do GitHub.

### Entregas desta Sprint
- Importação do dataset `pull_requests.csv` no Power BI.  
- Criação das primeiras visualizações exploratórias (gráficos de distribuição e resumo estatístico):  
  - Distribuição do tempo de análise dos PRs (`AnalysisTimeHours`)  
  - Distribuição do tamanho dos PRs (`Additions` + `Deletions`)  
  - Distribuição do número de revisões (`Reviews`)  
  - Distribuição do número de interações (`Comments`, `Participants`, `Reviews`)  
- Inserção de descrições e títulos explicativos no dashboard.

Essas visualizações permitem compreender **as características gerais do conjunto de dados**, servindo de base para as próximas etapas, que envolvem responder às questões de pesquisa (RQs).

---

## Próximos Passos
Na próxima sprint (**Lab04S02**), serão adicionadas visualizações que respondem às **RQs 1 e 2**, analisando a relação entre:
1. O **tamanho** dos PRs e o **feedback final** (merged ou closed);  
2. O **tempo de análise** e o **feedback final** das revisões.

---

## Ferramentas Utilizadas
- **Python (Pandas / Seaborn / Matplotlib)** – para pré-processamento e exploração inicial.  
- **Power BI** – para construção do dashboard interativo e visualização final dos dados.  


