from gfxinfo_parser import GFXInfoParser
from tester import Tester
from utils import syscall

class RNTester(Tester):
    def __init__(self, config, record_screen=False) -> None:
        super().__init__(config, record_screen)
        self.app_id = f'com.rn.{config["app"]}'
        self.parser = GFXInfoParser()

    def tear_down(self):
        pass

    def reset(self):
        super().reset()
        print('Resetting frames...')
        syscall(f'adb shell dumpsys gfxinfo {self.app_id} reset')

    def read_frames(self) -> dict:
        print('Reading frames...')
        res = syscall(f'adb shell dumpsys gfxinfo {self.app_id}')
        return self.parser.parse_histogram(res.stdout)
