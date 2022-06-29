import json
import time


class Writer:
    def __init__(self, app_id) -> None:
        self.app_id = app_id

    def write(self, data):
        now = time.strftime("%Y%m%d-%H%M%S")
        file_name = f'outputs\{self.app_id}{now}.json'
        with open(file_name, 'w') as file:
            json.dump(data, file)