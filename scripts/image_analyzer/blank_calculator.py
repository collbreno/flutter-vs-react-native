from dataclasses import dataclass
import json
from math import ceil
import numpy as np
from frame_analyzer import FrameAnalyzer

@dataclass
class BlankInfo:
    '''Class for representing the estimation of 
    how many items from the list aren't been 
    rendered on the screen'''
    estimated_missing_items: int
    white_percentage: float
    white_relative_percentage: float

    def to_obj(self):
        return {
            'estimated_missing_items': self.estimated_missing_items,
            'white_percentage': self.white_percentage,
            'white_relative_percentage': self.white_relative_percentage
        }

class BlankCalulator:
    def __init__(self, framework) -> None:
        data = self.__read_specs_file()
        self.item_percentage = data[framework]['blank_item']
        self.list_percentage = data[framework]['all_blank']
        self.diff = 0.5

    def __read_specs_file(self):
        f = open('framework_specs/output.json')
        return json.load(f)

    def __estimate_missing_items(self, white_percentage):
        treated_percentage = white_percentage - self.diff
        if (treated_percentage < 0):
            return 0
        else:
            return ceil(treated_percentage/self.item_percentage)
        
    def __calculate_white_relative_percentage(self, white_percentage):
        return np.round((white_percentage/self.list_percentage)*100, 2)

    def get_stats(self, image_path) -> BlankInfo:
        analyzer = FrameAnalyzer(image_path)
        percentage = analyzer.get_white_percentage()
        info = BlankInfo(
            white_percentage=percentage,
            white_relative_percentage=self.__calculate_white_relative_percentage(percentage),
            estimated_missing_items=self.__estimate_missing_items(percentage),
        )
        return info

    