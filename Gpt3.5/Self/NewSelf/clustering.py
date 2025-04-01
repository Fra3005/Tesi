import re
import os
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoTokenizer, AutoModel
import torch

def get_embeddings(responses, model_name='bert-base-uncased'):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    
    inputs = tokenizer(responses, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings.numpy()

def process_question_files(input_dir, output_file_path):
    """
    Elabora 13 file di domande, esegue il clustering DBSCAN su ciascun set di risposte
    e salva le risposte selezionate in un nuovo file, con informazioni sui cluster.
    """
    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for question_num in range(1, 21):
                input_file_path = os.path.join(input_dir, f"Question{question_num}.txt")
                if not os.path.exists(input_file_path):
                    print(f"File non trovato: {input_file_path}")
                    continue

                with open(input_file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                matches = re.findall(r"=== Answer \(Risposta: (\d+)\) ===\n(.*?)(?=\n=== Answer|\Z)", content, re.DOTALL)
                if not matches:
                    print(f"Nessuna risposta trovata in: {input_file_path}")
                    continue

                temperature_responses = {int(temperature): response.strip() for temperature, response in matches}
                responses = list(temperature_responses.values())

                embeddings = get_embeddings(responses)
                similarity_matrix = cosine_similarity(embeddings)
                distance_matrix = 1 - similarity_matrix
                clustering = DBSCAN(metric="cosine", eps=0.2, min_samples=2).fit(distance_matrix)
                labels = clustering.labels_

                unique_labels = np.unique(labels[labels != -1])
                num_clusters = len(unique_labels)

                unique_labels, counts = np.unique(labels[labels != -1], return_counts=True)
                if len(unique_labels) == 0:
                    best_response = "Nessun cluster trovato, risposte troppo diverse."
                    best_temp = "N/A"
                    best_cluster = "N/A"
                else:
                    largest_cluster = unique_labels[np.argmax(counts)]
                    cluster_indices = [i for i in range(len(responses)) if labels[i] == largest_cluster]
                    avg_similarities = similarity_matrix[cluster_indices].mean(axis=1)
                    best_index = cluster_indices[np.argmax(avg_similarities)]
                    best_response = responses[best_index]
                    best_temp = list(temperature_responses.keys())[list(temperature_responses.values()).index(best_response)]
                    best_cluster = labels[best_index]

                output_file.write(f"Question {question_num} (Risposta: {best_temp}) - Cluster di appartenenza: {best_cluster}, Cluster Trovati: {num_clusters}\n{best_response}\n\n")

        print(f"Risposte selezionate salvate in: {output_file_path}")

    except Exception as e:
        print(f"Errore durante l'elaborazione dei file: {e}")

# Esempio di utilizzo:
input_directory = 'Gpt3.5\\Self\\NewSelf'  # Sostituisci con il percorso della tua cartella con i file di domande
output_file = 'Gpt3.5\\Self\\NewSelf\\selected_responses.txt'
process_question_files(input_directory, output_file)