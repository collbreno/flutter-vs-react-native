from time import sleep
import os
import signal
import subprocess
import time
from rn_tester import RNTester
from utils import syscall


class RNRecTester(RNTester):
    def __init__(self, config) -> None:
        super().__init__(config)
        self.histogram_writer.app_id = self.app_id.replace('rn', 'rn_rec')

    def reset(self):
        super().reset()
        subprocess.Popen('adb shell screenrecord /sdcard/video.mp4')

    def read_frames(self) -> dict:
        self.__save_video()
        return super().read_frames()

    def __save_video(self):
        app_id = self.histogram_writer.app_id
        syscall('adb shell pkill -2 screenrecord')
        now = time.strftime("%Y%m%d-%H%M%S")
        folder_path = f'outputs/{app_id}'
        os.makedirs(folder_path, exist_ok=True)
        file_name = f"{folder_path}/{app_id}-{now}.mp4"
        sleep(3)
        print(syscall(f"adb pull /sdcard/video.mp4 {file_name}"))
        print(syscall("adb shell rm /sdcard/video.mp4"))
