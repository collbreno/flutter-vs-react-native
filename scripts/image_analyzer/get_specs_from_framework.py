import cv2
from frame_analyzer import FrameAnalyzer

def get_input_image_name(framework, suffix):
    return f'./images/{framework}_{suffix}.png'

def get_output_image_name(framework, suffix):
    return f'./framework_specs/{framework}_{suffix}.png'

def write_line(line):
        file.write(','.join(line))
        file.write('\n')

if __name__ == '__main__':

    header = ['framework', 'all_blank', 'blank_item']
    lines = []
    for framework in ['rn', 'flutter']:
        line = [framework]
        for spec_type in ['all_blank', 'blank_item']:

            img = get_input_image_name(framework, spec_type)

            analyzer = FrameAnalyzer(img)

            analyzer.save_masked(
                get_output_image_name(framework, spec_type)
            )

            white_percentage = analyzer.get_white_percentage()

            line.append(str(white_percentage))
        lines.append(line)
    
    with open('./framework_specs/output.csv', 'w') as file:
        write_line(header)
        for line in lines:
            write_line(line)