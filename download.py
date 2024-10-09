import json
import os
import requests

with open('tchmaterial.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for subject in data:
    if not os.path.exists(subject):
        os.makedirs(subject)
    for chapter in data[subject]:
        with open(os.path.join(subject, chapter + '.pdf'), 'wb') as f:
            print(f'正在下载 {subject} {chapter}...')
            f.write(requests.get(data[subject][chapter]).content)