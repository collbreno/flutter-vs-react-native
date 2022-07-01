import json
import sys

from gfxinfo_parser import GFXInfoParser
from tester import RNTester, FlutterTester, Tester

def get_file_name():
    args = sys.argv
    if len(args) < 2:
        raise Exception('Config file name not defined')
    return args[1]

def get_framework():
    args = sys.argv
    if len(args) < 3:
        raise Exception('Framework not defined')
    return args[2]

def get_n_of_executions():
    args = sys.argv
    if len(args) < 4:
        raise Exception('Number of executions not defined')
    return int(args[3])

def read_json():
    file = open(get_file_name())
    data = json.load(file)
    return data

def create_tester() -> Tester:
    data = read_json()
    framework = get_framework()
    if framework == 'rn':
        return RNTester(data)
    elif framework == 'flutter':
        return FlutterTester(data)
    else:
        raise Exception("Framework must be rn or flutter")

if __name__ == '__main__':
    n = get_n_of_executions()
    tester = create_tester()
    tester.set_up()
    for i in range(n):
        tester.run()
    tester.tear_down()