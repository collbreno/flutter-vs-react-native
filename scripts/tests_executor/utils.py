import subprocess
import glob
import json
import os
from pathlib import Path

def syscall(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def get_last_download():
    list_of_files = glob.glob(str(os.path.join(Path.home(), 'Downloads/*.json'))) # * means all if need specific format then *.csv
    return max(list_of_files, key=os.path.getctime)