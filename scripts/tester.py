from time import sleep
from flutter_devtools import FlutterDevTools
from gfxinfo_parser import GFXInfoParser
from utils import syscall
import abc

from writer import Writer


class Tester(metaclass=abc.ABCMeta):
    app_id: str
    writer: Writer

    def __init__(self, config) -> None:
        self.config = config
        self.parser = GFXInfoParser()

    def open_app(self):
        print('Opening app...')
        syscall(f'adb shell monkey -p {self.app_id} 1')
        sleep(1)

    @abc.abstractmethod
    def read_frames(self):
        raise NotImplementedError()

    def execute_commands(self):
        print('Executing commands...')
        for cmd in self.config['commands']:
            syscall(cmd)

    @abc.abstractmethod
    def set_up(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def tear_down(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def on_app_opened(self):
        raise NotImplementedError()

    def run(self):
        self.open_app()
        self.on_app_opened()
        self.execute_commands()
        sleep(self.config["cooldown"])
        frames = self.read_frames()
        self.writer.write(frames)

class RNTester(Tester):
    def __init__(self, config) -> None:
        super().__init__(config)
        self.app_id = f'com.rn.{config["app"]}'
        self.writer = Writer(self.app_id)

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def on_app_opened(self):
        print('Resetting frames...')
        syscall(f'adb shell dumpsys gfxinfo {self.app_id} reset')

    def read_frames(self):
        print('Reading frames...')
        res = syscall(f'adb shell dumpsys gfxinfo {self.app_id}')
        return self.parser.parse_histogram(res.stdout)

class FlutterTester(Tester):
    def __init__(self, config) -> None:
        super().__init__(config)
        self.app_id = f'com.flutter.{config["app"]}'
        self.writer = Writer(self.app_id)
        self.devtools = FlutterDevTools(config["flutter_devtools_url"])

    def set_up(self):
        self.devtools.open()

    def on_app_opened(self):
        self.devtools.reset_frames()
        pass

    def read_frames(self):
        self.devtools.export_data()

    def tear_down(self):
        self.devtools.close()