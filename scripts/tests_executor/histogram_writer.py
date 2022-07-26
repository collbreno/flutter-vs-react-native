import json
import os
import time

class HistogramWriter:

    def write(self, data, app_id):
        now = time.strftime("%Y%m%d-%H%M%S")
        folder_path = f'outputs/{app_id}'
        os.makedirs(folder_path, exist_ok=True)
        file_name = f'{folder_path}/{app_id}-{now}.json'
        with open(file_name, 'w') as file:
            json.dump(data, file)