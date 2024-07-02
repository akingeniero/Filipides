import os
import json
import pandas as pd
import matplotlib.pyplot as plt

folders = [
    '../reports_news_negatives',
    '../reports_news_positives',
    '../reports_tweets_negatives',
    '../reports_tweets_positives',
]

data = []

for folder in folders:
    for file_name in os.listdir(folder):
        if file_name.endswith('.json'):
            file_path = os.path.join(folder, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = json.load(file)
                review = content.get("review", "")
                analysis = content.get("analysis", {})
                elapsed_time = content.get("elapsed_time", None)
                if analysis and elapsed_time:
                    model = analysis.get("model", None)
                    data.append({
                        "model": model,
                        "elapsed_time": elapsed_time
                    })

df = pd.DataFrame(data)

mean_elapsed_time = df.groupby('model')['elapsed_time'].mean().reset_index()
sample_size = df.groupby('model')['elapsed_time'].count().reset_index()
mean_elapsed_time['sample_size'] = sample_size['elapsed_time']

plt.figure(figsize=(10, 6))
bars = plt.bar(mean_elapsed_time['model'], mean_elapsed_time['elapsed_time'], color='skyblue')
plt.xlabel('Model')
plt.ylabel('Mean Response Time')
plt.title('Mean Response Time by Model')
plt.xticks(rotation=45)

for bar, size in zip(bars, mean_elapsed_time['sample_size']):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'n={size}', ha='center', va='bottom')

plt.tight_layout()

output_folder = '.'
output_path = os.path.join(output_folder, 'analysis_response_time.png')
plt.savefig(output_path)

plt.show()

print(mean_elapsed_time)
