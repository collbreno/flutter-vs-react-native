from functools import reduce

class HistogramAnalyzer:
    def __init__(self) -> None:
        self.histogram = {}

    def __reduce_frames(self, acc, key):
        return acc + self.histogram[key]

    def __reduce_janky_frames(self, acc, key):
        return acc + self.histogram[key] if key > 16 else acc

    def merge(self, other: dict) -> None:
        for str_key in other.keys():
            key = int(str_key)
            if key not in self.histogram:
                self.histogram[key] = 0
            self.histogram[key] += other[str_key]

    def count_frames(self) -> int:
        return reduce(self.__reduce_frames, self.histogram, 0)
        
    def count_janky_frames(self) -> int:
        return reduce(self.__reduce_janky_frames, self.histogram, 0)

    def get_janky_frames_percentage(self) -> str:
        percentage = (self.count_janky_frames() / self.count_frames())*100.0
        return  "%.2f%%" % percentage

    def get_array(self) -> list:
        l = []
        for key in self.histogram.keys():
            count = self.histogram[key]
            for i in range(count):
                l.append(int(key))
        return l