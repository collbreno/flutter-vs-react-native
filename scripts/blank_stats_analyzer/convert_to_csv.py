from glob import glob
import json

import pandas as pd

def get_execution_id(file_name: str):
    i = file_name.find('rec-')
    return file_name[i+len('rec-'):-len('.json')]

def get_framework(file_name: str):
    i = file_name.find('com.')
    j = file_name.find('.list_rec')
    return file_name[i+len('com.'):j]

def get_json(file_name):
    f = open(file_name)
    return json.load(f)

if __name__ == '__main__':
    executions = glob('../image_analyzer/outputs/*/*.json')
    table = []
    columns = [
        'framework',
        'execution_id',
        'frame_id',
        'estimated_missing_items',
        'white_percentage',
        'white_relative_percentage'
    ]

    for execution in executions:
        execution_id = get_execution_id(execution)
        framework = get_framework(execution)
        data = get_json(execution)
        for i in range(len(data)):
            table.append([
                framework,
                execution_id,
                i,
                data[i]['estimated_missing_items'],
                data[i]['white_percentage'],
                data[i]['white_relative_percentage']
            ])
    df = pd.DataFrame(table, columns=columns)
    df.to_csv('dataframe.csv')

