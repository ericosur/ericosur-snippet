''' add border from a image '''

import os
from typing import Any

import cv2
from cv2.typing import MatLike
from imgconfig import prt, read_image_config

# to omit the warning
os.environ["QT_QPA_FONTDIR"] = "/usr/share/fonts/truetype/dejavu"

class Solution:
    ''' Solution class for adding border to an image '''

    config_key: str = "global"
    border_size: int = 80

    def __init__(self) -> None:
        ''' Initialize the Solution class '''
        self.border_size: int = Solution.border_size
        self.config: dict[str, Any] = read_image_config()
        self.image_path: str = self.__get_image_path()
        self.image_count: int = 0

    def __get_image_path(self) -> str:
        ''' get the full image path '''
        sett = self.config.get(self.config_key, "images")
        base_path = sett.get("image_base_dir")
        imgs = sett.get("images")
        if not isinstance(imgs, list):
            raise TypeError("Images configuration is not a list")

        filename = imgs[0] if imgs else ""
        fullpath = os.path.join(base_path, filename)
        if os.path.exists(fullpath):
            return fullpath
        else:
            raise FileNotFoundError(f"Image file not found: {fullpath}")

    def add_border(self, src: MatLike) -> MatLike:
        ''' add border '''
        borderType = cv2.BORDER_ISOLATED
        top = self.border_size
        bottom = self.border_size
        left = self.border_size // 2
        right = self.border_size // 2
        dst = cv2.copyMakeBorder(src, top, bottom, left, right, borderType)
        return dst

    def show_img(self, img: MatLike) -> None:
        ''' show image '''
        # img.shape = (height, width, channel)
        prt(f'img.shape (h,w,c): {img.shape}')
        name = f'image_{self.image_count}_{img.shape[1]}x{img.shape[0]}'
        cv2.namedWindow(name)
        if self.image_count > 0:
            cv2.moveWindow(name, img.shape[1]//3, img.shape[0]//3)
        cv2.imshow(name, img)
        self.image_count += 1

    @classmethod
    def run(cls, size: int) -> None:
        ''' set the border size for all instances '''
        cls.border_size = size
        obj = Solution()
        # image path from configuration
        src = cv2.imread(obj.image_path)
        if src is None:
            raise OSError(f"Unable to load image: {obj.image_path}")
        obj.show_img(src)

        dst = obj.add_border(src)
        obj.show_img(dst)

def main() -> None:
    ''' main '''
    Solution.run(80)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
