from frame_analyzer import FrameAnalyzer
from blank_calculator import BlankCalulator

calculator = BlankCalulator('rn')
for i in range(1, 15):
    t = str(i).zfill(3)
    file = f'../frames/frame{t}.png'
    print(calculator.get_stats(file))
    FrameAnalyzer(file).show_masked()