import base64
from io import BytesIO
from PIL import Image, ImageEnhance
import re

class ImageDarkener:
    def __init__(self) -> None:
        self.factor = 0.8
        self.prefix = 'data:image/png;base64,'

    def darken(self, input_img):
        base64_img = re.sub('^data:image/.+;base64,', '', input_img)

        img = Image.open(BytesIO(base64.b64decode(base64_img)))
        enhancer = ImageEnhance.Brightness(img)
        output = enhancer.enhance(self.factor)

        buff = BytesIO()
        output.save(buff, format="PNG")
        img_str = base64.b64encode(buff.getvalue())
        return self.prefix + img_str.decode()

