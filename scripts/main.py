import json
import sys

from gfxinfo_parser import GFXInfoParser
from tester import Tester

def get_file_name():
    args = sys.argv
    if len(args) < 2:
        raise Exception('Config file name not defined')
    return args[1]

def read_json():
    file = open(get_file_name())
    data = json.load(file)
    return data

if __name__ == '__main__':
    data = read_json()
    Tester(data).test()
