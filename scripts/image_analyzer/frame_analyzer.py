import cv2
import numpy as np

# Inspired in code from @stateMachine
# https://stackoverflow.com/a/66757536/11313788

class FrameAnalyzer:
    def __init__(self, image_path) -> None:
        target_color = [247, 249, 246]
        diff = 5
        # Be aware that opencv loads image in BGR format,
        # that's why the color values have been adjusted here:
        self.boundaries = ([target_color[2], target_color[1]-diff, target_color[0]-diff],
           [target_color[2]+diff, target_color[1]+diff, target_color[0]+diff])
        self.scale_percent = 0.3
        self.image = self.__get_resized_img(image_path)
        self.mask = self.__get_mask()

    def __get_resized_img(self, image_path):
        img = cv2.imread(image_path)
        width = int(img.shape[1] * self.scale_percent)
        height = int(img.shape[0] * self.scale_percent)
        newSize = (width, height)
        return cv2.resize(img, newSize, None, None, None, cv2.INTER_AREA)

    def __get_mask(self):
        (lower, upper) = self.boundaries
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)

        # cv2.inRange is used to binarize (i.e., render in white/black) an image
        # All the pixels that fall inside your interval [lower, uipper] will be white
        # All the pixels that do not fall inside this interval will
        # be rendered in black, for all three channels:
        return cv2.inRange(self.image, lower, upper)

    def get_white_percentage(self):
        # You can use the mask to count the number of white pixels.
        # Remember that the white pixels in the mask are those that
        # fall in your defined range, that is, every white pixel corresponds
        # to a white pixel. Divide by the image size and you got the
        # percentage of white pixels in the original image:
        ratio_white = cv2.countNonZero(self.mask)/(self.image.size/3)
        color_percent = (ratio_white * 100)
        
        return color_percent

    def show_masked(self):
        output = cv2.bitwise_and(self.image, self.image, mask=self.mask)
        cv2.imshow("images", np.hstack([self.image, output]))
        cv2.waitKey(0)
