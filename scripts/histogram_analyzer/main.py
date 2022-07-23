import os
import seaborn as sns
import matplotlib.pyplot as plt
import glob
import json
from csv_writer import CSVWriter
from histogram_analyzer import HistogramAnalyzer

files = glob.glob('../tests_executor/outputs/*/*.json')
frameworks = ['rn', 'flutter']
apps = ['counter', 'list', 'navigations', 'stopwatch', 'multistopwatch']

os.makedirs('outputs/', exist_ok=True)

csv_writer = CSVWriter()
for framework in frameworks:
    for app in apps:
        analyzer = HistogramAnalyzer()
        for file_name in filter(lambda x: f'com.{framework}.{app}' in x, files):
            file = open(file_name)
            data = json.load(file)
            analyzer.merge(data)
        csv_writer.add_line(framework, app, analyzer)
        sns.histplot(analyzer.get_array(), discrete=True)
        plt.savefig(f'outputs/{framework}_{app}.png')
        # plt.show()
csv_writer.write()