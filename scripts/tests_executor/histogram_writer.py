import json
import os
import time

class HistogramWriter:
    def __init__(self, app_id) -> None:
        self.app_id = app_id

    def write(self, data):
        now = time.strftime("%Y%m%d-%H%M%S")
        folder_path = f'outputs/{self.app_id}'
        os.makedirs(folder_path, exist_ok=True)
        file_name = f'{folder_path}/{self.app_id}-{now}.json'
        with open(file_name, 'w') as file:
            json.dump(data, file)