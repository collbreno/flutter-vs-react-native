from gfxinfo_parser import GFXInfoParser
from tester import Tester
from histogram_writer import HistogramWriter
from utils import syscall

class RNTester(Tester):
    def __init__(self, config) -> None:
        super().__init__(config)
        self.app_id = f'com.rn.{config["app"]}'
        self.histogram_writer = HistogramWriter(self.app_id)
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
