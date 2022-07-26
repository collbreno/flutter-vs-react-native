from time import sleep
from screen_recorder import ScreenRecorder
from utils import syscall
import abc

from histogram_writer import HistogramWriter

class Tester(metaclass=abc.ABCMeta):
    app_id: str

    def __init__(self, config, record_screen=False) -> None:
        self.config = config
        self.histogram_writer = HistogramWriter()
        self.record_screen = record_screen
        self.recorder = ScreenRecorder()

    def get_output_app_id(self):
        return self.app_id+'_rec' if self.record_screen else self.app_id


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
        if self.record_screen:
            self.recorder.start()
        self.execute_commands()
        sleep(self.config["cooldown"])
        if self.record_screen:
            self.recorder.save_video(self.get_output_app_id())
        frames = self.read_frames()
        self.histogram_writer.write(frames, self.get_output_app_id())