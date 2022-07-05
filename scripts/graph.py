import seaborn as sns
import matplotlib.pyplot as plt
import glob
import json
import numpy as np

def convert_to_list(data):
    l = []
    for key in data.keys():
        count = data[key]
        for i in range(count):
            l.append(int(key))
    return l

files = glob.glob('outputs/*.json')
frameworks = ['rn', 'flutter']
apps = ['counter', 'list']

for framework in frameworks:
    for app in apps:
        app_list = []
        for file_name in filter(lambda x: f'com.{framework}.{app}' in x, files):
            file = open(file_name)
            data = json.load(file)
            l = sorted(convert_to_list(data))
            app_list.extend(l)
        sns.histplot(app_list, discrete=True)
        plt.savefig(f'graphs/{framework}_{app}.png', bbox_inches='tight')
        plt.show()
