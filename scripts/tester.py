from time import sleep
from gfxinfo_parser import GFXInfoParser
from utils import syscall


class Tester:
    def __init__(self, config) -> None:
        self.config = config
        self.app_id = f'com.rn.{config["app"]}'
        self.parser = GFXInfoParser()

    def open_app(self):
        print('Opening app...')
        syscall(f'adb shell monkey -p {self.app_id} 1')
        sleep(1)

    def reset_frames(self):
        print('Resetting frames...')
        syscall(f'adb shell dumpsys gfxinfo {self.app_id} reset')

    def read_frames(self):
        print('Reading app...')
        res = syscall(f'adb shell dumpsys gfxinfo {self.app_id}')
        parsed = self.parser.parse_histogram(res.stdout)
        print(parsed)

    def execute_commands(self):
        print('Executing commands...')
        for cmd in self.config['commands']:
            syscall(cmd)

    def test(self):
        self.open_app()
        self.reset_frames()
        self.execute_commands()
        self.read_frames()