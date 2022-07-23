import json
import cv2
import numpy as np
from frame_analyzer import FrameAnalyzer

def get_input_image_name(framework, suffix):
    return f'./images/{framework}_{suffix}.png'

def get_output_image_name(framework, suffix):
    return f'./framework_specs/{framework}_{suffix}.png'

if __name__ == '__main__':

    obj = {}
    for framework in ['rn', 'flutter']:
        obj[framework] = {}
        for spec_type in ['all_blank', 'blank_item']:
            img = get_input_image_name(framework, spec_type)
            analyzer = FrameAnalyzer(img)
            analyzer.save_masked(
                get_output_image_name(framework, spec_type)
            )
            white_percentage = analyzer.get_white_percentage()
            obj[framework][spec_type] = np.round(white_percentage, 2)
    
    f = open('framework_specs/output.json', 'w')
    json.dump(obj, f)