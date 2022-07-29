from time import sleep
import os
import subprocess
import time
from utils import syscall

class ScreenRecorder():
    def start(self):
        subprocess.Popen('adb shell screenrecord /sdcard/video.mp4')
        sleep(1)

    def save_video(self, app_id):
        syscall('adb shell pkill -2 screenrecord')
        now = time.strftime("%Y%m%d-%H%M%S")
        folder_path = f'outputs/{app_id}'
        os.makedirs(folder_path, exist_ok=True)
        file_name = f"{folder_path}/{app_id}-{now}.mp4"
        sleep(3)
        syscall(f"adb pull /sdcard/video.mp4 {file_name}")
        syscall("adb shell rm /sdcard/video.mp4")