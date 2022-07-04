from time import sleep
from devtools_runner import DevtoolsRunner
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
    def read_frames(self) -> dict:
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