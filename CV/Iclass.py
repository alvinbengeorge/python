import requests
import cv2, numpy as np

from typing import Tuple
from Errors import (
    WrongFormatError,
    BigXVal,
    BigYVal
)


class Image:
    def __init__(self, picture, url: bool = False):
        self.picture = cv2.imread(picture) if not url else self.from_url(picture)
        self.split = list(map(self.split_and_return, ['r', 'g', 'b']))

    def split_and_return(self, color: str = "r"):
        '''
        Type 'r' for red
             'g' for green
             'b' for blue
        '''
        b, g, r = cv2.split(self.picture)
        if color == 'r': return r
        if color == 'g': return g
        if color == 'b': return b

    def from_url(self, url: str):
        #image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return cv2.imdecode(np.asarray(bytearray(requests.get(url=url).content), dtype="uint8"), cv2.IMREAD_COLOR)


    def section(self, region: Tuple[int]):
        '''
        Basically crop
        x_start, x_end, y_start, y_end
        '''
        if len(region) not in [2, 4]:
            raise WrongFormatError("You need 2 or 4 integer values")
        if len(region) == 2:
            region = (0, region[0], 0, region[1])

        if all(map(lambda k: k>=self.picture.shape[0], [region[0], region[1]])):
            raise BigXVal(f"X Value from {region[:2]} is larger than the image X value. Shape: {self.picture.shape}")
        if all(map(lambda k: k>=self.picture.shape[1], [region[2], region[3]])):
            raise BigYVal(f"Y Value from {region[:2]} is larger than the image Y value. Shape: {self.picture.shape}")

        
        return self.picture[
            region[0]: region[1],
            region[2]: region[3]
        ]
        


    def simple_show(self, image, window_name = "Image"):
        cv2.imshow(window_name, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
