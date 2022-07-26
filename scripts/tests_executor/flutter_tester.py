import json
from devtools_parser import DevtoolsParser
from tester import Tester
from utils import get_last_download
from devtools_runner import DevtoolsRunner

class FlutterTester(Tester):
    def __init__(self, config, record_screen=False) -> None:
        super().__init__(config, record_screen)
        self.app_id = f'com.flutter.{config["app"]}'
        self.devtools_runner = DevtoolsRunner(config["flutter_devtools_url"])
        self.devtools_parser = DevtoolsParser()

    def set_up(self):
        super().open_app()
        self.devtools_runner.open()

    def reset(self):
        super().reset()
        self.devtools_runner.reset_frames()

    def read_frames(self) -> dict:
        self.devtools_runner.export_data()
        exported_data = open(get_last_download())
        data = json.load(exported_data)
        return self.devtools_parser.parse_histogram(data)

    def tear_down(self):
        self.devtools_runner.close()