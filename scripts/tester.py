from time import sleep
from utils import syscall
import abc

from writer import Writer

class Tester(metaclass=abc.ABCMeta):
    app_id: str
    writer: Writer

    def __init__(self, config) -> None:
        self.config = config

    def open_app(self):
        print('Opening app...')
        syscall(f'adb shell monkey -p {self.app_id} 1')
        sleep(3)

    @abc.abstractmethod
    def read_frames(self) -> dict:
        raise NotImplementedError()

    def execute_commands(self):
        print('Executing commands...')
        for cmd in self.config['commands']:
            syscall(cmd)

    def set_up(self):
        self.open_app()
        if 'setup' in self.config:
            print('Setting up...')
            for cmd in self.config['setup']:
                print(cmd)
                syscall(cmd)

    @abc.abstractmethod
    def tear_down(self):
        raise NotImplementedError()

    def reset(self):
        if 'reset' in self.config:
            syscall(self.config['reset'])
            sleep(self.config['cooldown'])

    def run(self):
        self.reset()
        self.execute_commands()
        sleep(self.config["cooldown"])
        frames = self.read_frames()
        self.writer.write(frames)