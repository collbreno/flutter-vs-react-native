from io import TextIOWrapper
from histogram_analyzer import HistogramAnalyzer


class CSVWriter:
    def __init__(self) -> None:
        self.lines = []
        self.header = []
        self.header.append('framework')
        self.header.append('application')
        self.header.append('total_frames')
        self.header.append('janky_frames')
        self.header.append('janky_percentage')

    def add_line(self, framework: str, app: str, histogram_analyzer: HistogramAnalyzer) -> None:
        line = []
        line.append(framework)
        line.append(app)
        line.append(str(histogram_analyzer.count_frames()))
        line.append(str(histogram_analyzer.count_janky_frames()))
        line.append(histogram_analyzer.get_janky_frames_percentage())
        self.lines.append(line)

    def write_line(self, file: TextIOWrapper, line: list):
        file.write(','.join(line))
        file.write('\n')

    def write(self):
        with open('outputs/test.csv', 'w') as csv:
            self.write_line(csv, self.header)
            for line in self.lines:
                self.write_line(csv, line)

