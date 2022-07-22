import json
from image_darkener import ImageDarkener

def read_json():
    f = open('mock_data.json')
    return json.load(f)

def write_json(data):
    output = open('output.json', 'w')
    json.dump(data, output)

if __name__ == '__main__':
    darkener = ImageDarkener()
    
    data = read_json()

    for i in range(len(data)):
        data[i]['image'] = darkener.darken(data[i]['image'])

    write_json(data)