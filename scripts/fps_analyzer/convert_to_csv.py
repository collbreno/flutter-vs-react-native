from glob import glob
import json

import pandas as pd
from tqdm import tqdm

def get_framework(file_name: str):
    return file_name.split('.')[1]

def get_app_name(file_name: str):
    aux = file_name.split('.')[2]
    return aux[:aux.find('-')]

def get_execution_id(file_name: str):
    return file_name[file_name.find('-')+1:file_name.find('.json')]

def get_histogram(file_path: str) -> dict:
    f = open(file_path)
    return json.load(f)

executions = glob('../tests_executor/outputs/*/*.json')

table = []
columns = [
    'framework',
    'app',
    'execution_id',
    'frame_id',
    'frame_time'
]
for execution_path in tqdm(executions):
    id = 0
    file_name = execution_path.split('\\')[-1]
    data = get_histogram(execution_path)
    for time in data.keys():
        count = data[time]
        for frame_id in range(count):
            table.append([
                get_framework(file_name),
                get_app_name(file_name),
                get_execution_id(file_name),
                frame_id,
                time,
            ])
    df = pd.DataFrame(table, columns=columns)
    df.to_csv('dataframe.csv')
