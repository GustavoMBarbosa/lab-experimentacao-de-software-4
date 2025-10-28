import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==============================
# Configurações
# ==============================
sns.set_theme(style="whitegrid", palette="pastel")
CSV_INPUT = "arquivos/pull_requests.csv"
OUTPUT_DIR = "graficos"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==============================
# Leitura e limpeza
# ==============================
df = pd.read_csv(CSV_INPUT)
df.columns = [c.strip() for c in df.columns]

df["PR_Size"] = df["Additions"] + df["Deletions"]

print(f"Total de PRs: {len(df)}")
print(f"Repositórios distintos: {df['RepoName'].nunique()}")

# ==============================
# 1. PRs por repositório
# ==============================
plt.figure(figsize=(10,6))
top_repos = df["RepoName"].value_counts().head(10)
sns.barplot(x=top_repos.values, y=top_repos.index, palette="Blues_d")
plt.title("Top 10 repositórios com mais Pull Requests")
plt.xlabel("Quantidade de PRs")
plt.ylabel("Repositório")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/1_prs_por_repositorio.png")
plt.close()

# ==============================
# 2. Status dos PRs
# ==============================
plt.figure(figsize=(6,4))
sns.countplot(x="PR_Status", data=df, palette="pastel")
plt.title("Distribuição de Status dos Pull Requests")
plt.xlabel("Status (1=Merged, 0=Closed)")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/2_status_prs.png")
plt.close()

# ==============================
# 3. Tempo de análise (histograma)
# ==============================
plt.figure(figsize=(8,5))
sns.histplot(df["AnalysisTimeHours"], bins=40, color="skyblue", kde=True)
plt.title("Distribuição do Tempo de Análise (em horas)")
plt.xlabel("Tempo de análise (horas)")
plt.ylabel("Quantidade de PRs")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/3_tempo_analise.png")
plt.close()

# ==============================
# 4. Tamanho dos PRs (boxplot)
# ==============================
plt.figure(figsize=(8,5))
sns.boxplot(x=df["PR_Size"], color="lightcoral")
plt.title("Distribuição do Tamanho dos PRs (Linhas Alteradas)")
plt.xlabel("Total de Linhas Alteradas")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/4_tamanho_prs.png")
plt.close()

# ==============================
# 5. Revisões por PR
# ==============================
plt.figure(figsize=(8,5))
sns.histplot(df["Reviews"], bins=20, color="orange", kde=True)
plt.title("Distribuição do Número de Revisões por PR")
plt.xlabel("Número de Revisões")
plt.ylabel("Quantidade de PRs")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/5_revisoes_pr.png")
plt.close()

# ==============================
# 6. Correlação geral
# ==============================
plt.figure(figsize=(8,6))
corr_cols = ["PR_Size", "AnalysisTimeHours", "Participants", "Comments", "Reviews"]
sns.heatmap(df[corr_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlação entre Principais Métricas")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/6_correlacao_metricas.png")
plt.close()

print("Gráficos de caracterização do dataset gerados com sucesso!")
