import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import seaborn as sns

def preprocess_df(df):
    """Pre-elabora il DataFrame per standardizzare i nomi delle colonne e le risposte."""
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]  # Standardizza i nomi delle colonne
    for col in df.columns[3:]:  # Itera sulle colonne delle risposte
        if df[col].dtype == 'object':
            df[col] = df[col].str.lower().str.strip()  # Standardizza le risposte solo se sono stringhe
    return df

def compute_distribution(df):
    distributions = []
    for (categoria, tecnica), group in df.groupby(["category", "prompting_technique"]): #Nota che ho messo in minuscolo categoria e tecnica
        counts = Counter(group.iloc[:, 3:].values.flatten())
        total = sum(counts.values())

        if total == 0:
            distributions.append({
                "Categoria": categoria,
                "Tecnica": tecnica,
                "Answer %": 0.0,
                "Warning with %": 0.0,
                "Warning without %": 0.0,
                "No Answer %": 0.0,
            })
        else:
            distributions.append({
                "Categoria": categoria,
                "Tecnica": tecnica,
                "Answer %": (counts.get("answer", 0) / total) * 100,
                "Warning with %": (counts.get("warning with recommendations", 0) / total) * 100,
                "Warning without %": (counts.get("warning without recommendations", 0) / total) * 100,
                "No Answer %": (counts.get("no answer", 0) / total) * 100,
            })

    return pd.DataFrame(distributions)

# Carica il DataFrame dal file CSV
df = pd.read_csv("Gemini.csv", sep=";")

# Pre-elabora il DataFrame
df = preprocess_df(df)

# Calcola la distribuzione
distributions_df = compute_distribution(df)

distributions_df.to_csv("csv.csv")

# Stampa il risultato
print(distributions_df)

df = pd.read_csv("Gemini.csv", sep=";")

# Rinomina le colonne per rimuovere gli spazi
df.columns = df.columns.str.replace(" ", "_")

# Funzione per creare un grafico a torta per un modello specifico
def create_pie_chart(df, model_column, title):
    response_counts = df[model_column].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(response_counts, labels=response_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')  # Assicura che la torta sia disegnata come un cerchio
    plt.show()

# Crea grafici a torta per ciascun modello
create_pie_chart(df, "Gemini", "Distribuzione risposte Gemini")
create_pie_chart(df, "Llama", "Distribuzione risposte Llama")
create_pie_chart(df, "Gpt3.5", "Distribuzione risposte GPT-3.5")




# # 🔹 Funzione per calcolare l'Agreement Score
# def calculate_agreement(df):
#     agreement_scores = []
#     for (categoria, tecnica), group in df.groupby(["Categoria", "Tecnica"]):
#         agreement_values = []
#         for _, row in group.iterrows():
#             counts = Counter(row[3:].values)  # Conta le risposte dei modelli
#             most_common = counts.most_common(1)[0][1]
#             agreement_values.append(most_common / len(modelli))  # Divisione per il numero di modelli
#         agreement_scores.append({
#             "Categoria": categoria,
#             "Tecnica": tecnica,
#             "Agreement Score": sum(agreement_values) / len(agreement_values)
#         })
#     return pd.DataFrame(agreement_scores)

# df_agreement = calculate_agreement(df)

# # 🔹 Funzione per calcolare Cohen’s Kappa tra modelli per ogni categoria e tecnica
# def compute_kappa(df):
#     kappa_results = []
#     for (categoria, tecnica), group in df.groupby(["Categoria", "Tecnica"]):
#         model_data = group.iloc[:, 3:].values.tolist()  # Prendi solo le risposte dei modelli
#         kappa_scores = []
#         for i, j in combinations(range(len(modelli)), 2):  # Tutte le combinazioni di 2 modelli
#             kappa = cohen_kappa_score([row[i] for row in model_data], [row[j] for row in model_data])
#             if kappa is not None:  # Evita errori con dati troppo omogenei
#                 kappa_scores.append(kappa)
#         if kappa_scores:
#             kappa_results.append({
#                 "Categoria": categoria,
#                 "Tecnica": tecnica,
#                 "Cohen's Kappa": sum(kappa_scores) / len(kappa_scores)
#             })
#     return pd.DataFrame(kappa_results)

# df_kappa = compute_kappa(df)

# # 🔹 Mostra i risultati
# print("\n📊 Distribuzione delle risposte per categoria e tecnica:")
# print(df_distribution)

# print("\n📊 Agreement Score per categoria e tecnica:")
# print(df_agreement)

# print("\n📊 Cohen’s Kappa per categoria e tecnica:")
# print(df_kappa)
