from glob import glob
import json
import os
from tqdm import tqdm
from blank_calculator import BlankCalulator

folders = glob('./frames/*/*')
for folder in folders:
    stats_list = []
    execution_id = folder.split('\\')[-1]
    framework = execution_id.split('.')[1]
    frames = glob(f'{folder}/*.png')
    blank_calculator = BlankCalulator(framework)
    for frame in tqdm(frames):
        stats = blank_calculator.get_stats(frame).to_obj()
        stats_list.append(stats)
    output_folder_path = f"./outputs/{execution_id.split('-')[0]}"
    os.makedirs(output_folder_path, exist_ok=True)
    output_file = open(f'{output_folder_path}/{execution_id}.json', 'w')
    json.dump(stats_list, output_file)