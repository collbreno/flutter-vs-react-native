from tester import Tester
from writer import Writer
from utils import syscall

class RNTester(Tester):
    def __init__(self, config) -> None:
        super().__init__(config)
        self.app_id = f'com.rn.{config["app"]}'
        self.writer = Writer(self.app_id)

    def tear_down(self):
        pass

    def on_app_opened(self):
        print('Resetting frames...')
        syscall(f'adb shell dumpsys gfxinfo {self.app_id} reset')

    def read_frames(self) -> dict:
        print('Reading frames...')
        res = syscall(f'adb shell dumpsys gfxinfo {self.app_id}')
        return self.parser.parse_histogram(res.stdout)
