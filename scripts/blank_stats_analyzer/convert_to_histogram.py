from glob import glob
import json
import seaborn as sns
import matplotlib.pyplot as plt

folders = glob('../image_analyzer/outputs/*')

for folder in folders:
    estimated_missing_items = []
    executions = glob(f'{folder}/*.json')
    for execution in executions:
        file = open(execution)
        data = json.load(file)
        for item in data:
            estimated_missing_items.append(item['estimated_missing_items'])
    sns.histplot(estimated_missing_items, discrete=True)
    plt.show()
    x = []
    for i in range(0, len(estimated_missing_items)):
        x.append(i)
    y = estimated_missing_items
    sns.lineplot(x=x, y=y)
    plt.show()
