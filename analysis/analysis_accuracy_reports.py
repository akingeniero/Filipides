import os
import json
import pandas as pd
import matplotlib.pyplot as plt


path_negatives_1 = "../reports_tweets_negatives"
path_negatives_2 = "../reports_news_negatives"
path_positives_1 = "../reports_tweets_positives"
path_positives_2 = "../reports_news_positives"

def parse_json_files(directory, keywords):
    results = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if isinstance(data, dict) and 'analysis' in data:
                            model = data['analysis']['model']
                            if model not in results:
                                results[model] = {"correct": 0, "incorrect": 0}

                            if 'choices' in data['analysis']:
                                content = data['analysis']['choices'][0]['message']['content']
                            else:
                                content = data['analysis']['message']['content']

                            if any(keyword in content.lower() for keyword in keywords):
                                results[model]["correct"] += 1
                            else:
                                results[model]["incorrect"] += 1
                except (json.JSONDecodeError, KeyError, TypeError) as e:
                    print(f"Error processing file {file}: {e}")
    return results


negative_keywords = ["negativo", "malo", "infeliz", "triste"]
positive_keywords = ["positivo", "positiva", "alegre", "feliz"]


results_neg_1 = parse_json_files(path_negatives_1, negative_keywords)
results_neg_2 = parse_json_files(path_negatives_2, negative_keywords)


results_pos_1 = parse_json_files(path_positives_1, positive_keywords)
results_pos_2 = parse_json_files(path_positives_2, positive_keywords)


combined_results_neg = {}
for key in set(results_neg_1.keys()).union(results_neg_2.keys()):
    combined_results_neg[key] = {
        "Correct": results_neg_1.get(key, {}).get("correct", 0) + results_neg_2.get(key, {}).get("correct", 0),
        "Incorrect": results_neg_1.get(key, {}).get("incorrect", 0) + results_neg_2.get(key, {}).get("incorrect", 0),
    }


combined_results_pos = {}
for key in set(results_pos_1.keys()).union(results_pos_2.keys()):
    combined_results_pos[key] = {
        "Correct": results_pos_1.get(key, {}).get("correct", 0) + results_pos_2.get(key, {}).get("correct", 0),
        "Incorrect": results_pos_1.get(key, {}).get("incorrect", 0) + results_pos_2.get(key, {}).get("incorrect", 0),
    }


df_results_neg = pd.DataFrame(combined_results_neg).T
df_results_pos = pd.DataFrame(combined_results_pos).T


fig_neg, ax_neg = plt.subplots(figsize=(10, 6))
df_results_neg.plot(kind='bar', ax=ax_neg)
ax_neg.set_title('Correct and Incorrect by Model (Negative)')
ax_neg.set_xlabel('Models')
ax_neg.set_ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('analysis_accuracy_negatives_reports.png')
plt.show()


fig_pos, ax_pos = plt.subplots(figsize=(10, 6))
df_results_pos.plot(kind='bar', ax=ax_pos)
ax_pos.set_title('Correct and Incorrect by Model (Positive)')
ax_pos.set_xlabel('Models')
ax_pos.set_ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('analysis_accuracy_positive_reports.png')
plt.show()
