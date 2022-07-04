from tester import Tester
from writer import Writer
from devtools_runner import DevtoolsRunner

class FlutterTester(Tester):
    def __init__(self, config) -> None:
        super().__init__(config)
        self.app_id = f'com.flutter.{config["app"]}'
        self.writer = Writer(self.app_id)
        self.devtools = DevtoolsRunner(config["flutter_devtools_url"])

    def set_up(self):
        self.devtools.open()

    def on_app_opened(self):
        self.devtools.reset_frames()

    def read_frames(self) -> dict:
        self.devtools.export_data()

    def tear_down(self):
        self.devtools.close()