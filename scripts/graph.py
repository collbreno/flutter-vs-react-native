import seaborn as sns
import matplotlib.pyplot as plt
import glob
import json
from csv_writer import CSVWriter

from histogram_analyzer import HistogramAnalyzer

files = glob.glob('outputs/*.json')
frameworks = ['rn', 'flutter']
apps = ['counter', 'list', 'navigations', 'stopwatch', 'multistopwatch']

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
        plt.savefig(f'graphs/{framework}_{app}.png', bbox_inches='tight')
        # plt.show()
csv_writer.write()