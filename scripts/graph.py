import seaborn as sns
import matplotlib.pyplot as plt
import glob
import json

from histogram_analyzer import HistogramAnalyzer

files = glob.glob('outputs/*.json')
frameworks = ['rn', 'flutter']
apps = ['counter', 'list']

for framework in frameworks:
    for app in apps:
        analyzer = HistogramAnalyzer({})
        for file_name in filter(lambda x: f'com.{framework}.{app}' in x, files):
            file = open(file_name)
            data = json.load(file)
            analyzer.merge(data)
        sns.histplot(analyzer.get_array(), discrete=True)
        plt.savefig(f'graphs/{framework}_{app}.png', bbox_inches='tight')
        plt.show()
