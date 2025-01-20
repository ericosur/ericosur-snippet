#!/usr/bin/env python3
# coding: utf-8

''' collect import '''

import os
import re
import sys
from loguru import logger

#log_level = "DEBUG"
#log_format = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS zz}</green> | "
# "<level>{level: <8}</level> | <yellow>Line {line: >4} ({file}):</yellow> "
# "<b>{message}</b>"
# logger.add(sys.stderr, level=log_level, format=log_format, colorize=True, "
# "backtrace=True, diagnose=True)
# logger.add("file.log", level=log_level, format=log_format, colorize=False, "
# "backtrace=True, diagnose=True)
#logger.add(sys.stderr, level=log_level, colorize=False, backtrace=True, "
# "diagnose=True)
#logger.add("imports.log", level=log_level, colorize=False, backtrace=True, "
# "diagnose=True)
logger.add("debug.log", rotation="10MB", retention="7 days", level="DEBUG")
logd = logger.debug

sys.path.insert(0, "./")
sys.path.insert(0, "../")
sys.path.insert(0, "util/")
from the_config import official

class Solution():
    ''' class to grep the import '''
    def __init__(self, fn):
        self.imports = set()
        self.listfile = fn
        self._load_list()

    def _load_list(self):
        ''' load list from text file '''
        logd(f"load list from: {self.listfile}...")
        with open(self.listfile, "rt", encoding="UTF-8") as fin:
            cnt = 0
            for ln in fin.readlines():
                ln = ln.strip()
                if not os.path.isfile(ln):
                    print(f'file not found: {ln}')
                if "__init__" in ln:
                    logd(f"skip file: {ln}")
                    continue
                self.process(ln)
                cnt += 1
            logd(f"no of processed: {cnt}")

    def process(self, py_file: str) -> None:
        ''' process py file '''
        try:
            with open(py_file, "rt", encoding='UTF-8') as fobj:
                for pyln in fobj.readlines():
                    pyln = pyln.strip()
                    m1 = re.match(r"^\s*import (\S+)", pyln)
                    if m1:
                        v = m1.group(1)
                        if v in official:
                            #logd(f"skip value: {v}")
                            continue
                        if not v in self.imports:
                            logd(f"{py_file}: {v}")
                            self.imports.add(v)
                        continue
                    m2 = re.match(r"\s*from (\S+) import", pyln)
                    if m2:
                        v = m2.group(1)
                        if v in official:
                            #logd(f"skip value: {v}")
                            continue
                        if not v in self.imports:
                            logd(f"{py_file}: {v}")
                            self.imports.add(v)
        except UnicodeDecodeError:
            logger.error(f"unicode decode error on file: {py_file}")

    def show_result(self):
        ''' show '''
        res = list(self.imports)
        res.sort()
        print(res)
        # for i in self.imports:
        #     print(i)
        logger.critical(f"len: {len(res)}")

    @classmethod
    def run(cls, fn):
        ''' run '''
        logd(f"start run, list file: {fn}...")
        obj = cls(fn)
        obj.show_result()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        Solution.run(sys.argv[1])
    else:
        logd('need specify list file...')
