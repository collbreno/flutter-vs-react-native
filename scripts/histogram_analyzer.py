from functools import reduce

class HistogramAnalyzer:
    def __init__(self, histogram: dict) -> None:
        self.histogram = histogram

    def __reduce_frames(self, acc, key):
        return acc + self.histogram[key]

    def __reduce_janky_frames(self, acc, key):
        return acc + self.histogram[key] if key > 16 else acc

    def merge(self, other: dict) -> None:
        for key in other.keys():
            if key not in self.histogram:
                self.histogram[key] = 0
            self.histogram[key] += other[key]

    def count_frames(self) -> int:
        return reduce(self.__reduce_frames, self.histogram, 0)
        
    def count_janky_frames(self) -> int:
        return reduce(self.__reduce_janky_frames, self.histogram, 0)

    def get_janky_frames_percentage(self) -> str:
        return  "%.2f%%" % float(self.count_janky_frames() / self.count_frames())

    def get_array(self) -> list:
        l = []
        for key in self.histogram.keys():
            count = self.histogram[key]
            for i in range(count):
                l.append(int(key))
        return l