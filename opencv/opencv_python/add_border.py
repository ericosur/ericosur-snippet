''' add border from a image '''

import os
import sys
from random import choice
from typing import Any

import cv2
from cv2.typing import MatLike

# to omit the warning
if os.path.isdir('/usr/share/fonts/truetype/dejavu'):
    os.environ['QT_QPA_FONTDIR'] = '/usr/share/fonts/truetype/dejavu'

try:
    from imgconfig import prt, read_image_config
except ImportError:
    print('[INFO] imgconfig not found, exit...')
    sys.exit(1)


class Solution:
    ''' Solution class for adding border to an image '''

    config_key: str = 'global'

    def __init__(
        self,
        border_size: int = 80,
        image_path: str | None = None,
    ) -> None:
        ''' Initialize the Solution class '''
        self.border_size: int = border_size
        self.config: dict[str, Any] = read_image_config()
        self.image_path: str = image_path or self._get_image_path()
        self.image_count: int = 0

    def _get_image_path(self) -> str:
        ''' get the full image path '''
        sett = self.config.get(self.config_key, {})
        base_path = sett.get('image_base_dir')
        if not base_path or not os.path.exists(base_path):
            raise FileNotFoundError(f'image_base_dir not found: {base_path}')

        imgs = sett.get('images')
        if not isinstance(imgs, list) or not imgs:
            msg = f"No valid image list found under key '{self.config_key}'"
            raise ValueError(msg)

        fullpath = os.path.join(base_path, choice(imgs))
        if not os.path.exists(fullpath):
            raise FileNotFoundError(f'Image file not found: {fullpath}')
        return fullpath

    def add_border(
        self,
        src: MatLike,
        border_type: int = cv2.BORDER_CONSTANT,
        color: tuple[int, int, int] = (0, 0, 0),
    ) -> MatLike:
        ''' add border '''
        top = bottom = self.border_size
        left = right = self.border_size // 2
        return cv2.copyMakeBorder(
            src, top, bottom, left, right, border_type, value=color
        )

    def show_img(self, img: MatLike) -> None:
        ''' show image '''
        # img.shape = (height, width, channel)
        prt(f'img.shape (h,w,c): {img.shape}')
        name = f'image_{self.image_count}_{img.shape[1]}x{img.shape[0]}'
        cv2.namedWindow(name)
        if self.image_count > 0:
            cv2.moveWindow(name, img.shape[1] // 3, img.shape[0] // 3)
        cv2.imshow(name, img)
        self.image_count += 1

    @classmethod
    def run(cls, size: int = 80) -> None:
        ''' set the border size for all instances '''
        obj = cls(border_size=size)
        src = cv2.imread(obj.image_path)
        if src is None:
            raise OSError(f'Unable to load image: {obj.image_path}')

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
