class GFXInfoParser():
    def parse_histogram(self, output: str):
        histogram_begin = output.find('HISTOGRAM')
        first_number = output.find('ms', histogram_begin) - 1
        last_number = output.find('\n', histogram_begin)
        histogram_string = output[first_number:last_number]
        numbers = histogram_string.split(' ')
        histogram_dict = {}
        for number in numbers:
            [index, quantity] = map(lambda x: int(x), number.split('ms='))
            if quantity != 0:
                histogram_dict[index] = quantity
        return histogram_dict
