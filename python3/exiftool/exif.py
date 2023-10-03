#!/usr/bin/env python3
# coding: utf-8

'''
demo of module PyExifTool
'''

import os
import sys
from glob import glob

USE_TOML = False
try:
    import toml
    USE_TOML = True
except ImportError:
    print('[INFO] no toml function')

try:
    from exiftool import ExifToolHelper
except ImportError:
    print('pip install PyExifTool')
    sys.exit(1)

class Solution():
    ''' solution for extract GPS '''
    queries = ["EXIF:GPSLatitude", "EXIF:GPSLatitudeRef",
               "EXIF:GPSLongitude", "EXIF:GPSLongitudeRef"]

    def __init__(self, conf):
        self.picdirs = []
        self.conf = conf
        if USE_TOML:
            self._load_picdirs()
        else:
            self.picdirs.append(self._get_path())

    def _load_picdirs(self):
        ''' load picdirs from config file '''
        if not os.path.exists(self.conf):
            print('[ERROR] config file not found')
            sys.exit(1)
        data = toml.load(self.conf)
        self.picdirs = data['picdirs']

    def _get_path(self):
        home = os.getenv('HOME')
        ret = os.path.join(home, 'Pictures', '99.misc', 'Panoramdo')
        return ret

    def extract_gps(self, fn):
        ''' what '''
        ret = ''
        with ExifToolHelper() as et:
            [d] = et.get_metadata(fn)
            try:
                ret += f'{d["EXIF:GPSLatitude"]:.6f}{d["EXIF:GPSLatitudeRef"]} '
                ret += f'{d["EXIF:GPSLongitude"]:.6f}{d["EXIF:GPSLongitudeRef"]}'
            except KeyError:
                pass
        return ret

    @classmethod
    def run(cls, conf):
        ''' run '''
        obj = cls(conf)
        for d in obj.picdirs:
            if not os.path.exists(d):
                print(f'[ERROR] not such dir: {d}')
                continue
            d = os.path.join(d, "*.jpg")
            files = glob(d)
            for f in files:
                ret = obj.extract_gps(f)
                if ret:
                    print(f'{f}: {ret}')

def main():
    ''' main '''
    conf_file = 'config.toml'
    print('[INFO] read {conf_file} for pictures...', file=sys.stderr)
    Solution.run(conf=conf_file)

if __name__ == '__main__':
    main()
