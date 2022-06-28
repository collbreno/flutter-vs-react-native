from time import sleep
from gfxinfo_parser import GFXInfoParser
from utils import syscall
import abc


class Tester(metaclass=abc.ABCMeta):
    app_id: str

    def __init__(self, config) -> None:
        self.config = config
        self.parser = GFXInfoParser()

    def open_app(self):
        print('Opening app...')
        syscall(f'adb shell monkey -p {self.app_id} 1')
        sleep(1)

    @abc.abstractmethod
    def read_frames(self):
        raise NotImplementedError

    def execute_commands(self):
        print('Executing commands...')
        for cmd in self.config['commands']:
            syscall(cmd)

    @abc.abstractmethod
    def on_app_opened(self):
        raise NotImplementedError

    def run(self):
        self.open_app()
        self.on_app_opened()
        self.execute_commands()
        self.read_frames()

class RNTester(Tester):
    def __init__(self, config) -> None:
        super().__init__(config)
        self.app_id = f'com.rn.{config["app"]}'

    def on_app_opened(self):
        print('Resetting frames...')
        syscall(f'adb shell dumpsys gfxinfo {self.app_id} reset')

    def read_frames(self):
        print('Reading frames...')
        res = syscall(f'adb shell dumpsys gfxinfo {self.app_id}')
        parsed = self.parser.parse_histogram(res.stdout)
        print(parsed)

class FlutterTester(Tester):
    def __init__(self, config) -> None:
        super().__init__(config)
        self.app_id = f'com.flutter.{config["app"]}'

    def on_app_opened(self):
        pass

    def read_frames(self):
        pass #TODO: IMPLEMENT