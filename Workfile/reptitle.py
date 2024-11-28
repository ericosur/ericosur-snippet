#!/usr/bin/env python3
#coding: utf-8

'''
change the first line ```#/usr/bin/python```
to ```#/usr/bin/env python3```

use:
rg "/usr/bin/python" > list.txt
./reptitle.py
'''

import os
import re
import sys
from rich.console import Console
console = Console()
logd = console.log

class Solution:
    list_fn = "list.txt"

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

    def action(self):
        ''' action '''
        logd("action")
        self.process_list()

    def hack_file(self, fn: str):
        ''' hack file '''
        if not os.path.isfile(fn):
            logd(f'fail to hack {fn}')
        logd(f"hack_file: {fn}")
        is_modified = False
        try:
            with open(fn, "r+t", encoding="UTF-8") as ff:
                lines = ff.readlines()
                m = re.match(r'^#!/usr/bin/python(3)?', lines[0])
                if m:
                    lines[0] = "#!/usr/bin/env python3\n"
                    ff.seek(0)
                    ff.writelines(lines)
                    ff.truncate()
                    is_modified = True
        except UnicodeDecodeError as e:
            logd(f'[FAIL] decode error: {e}')
        if is_modified:
            logd(f'is modified: {fn}')

    def process_list(self):
        ''' process '''
        with open(self.list_fn, 'rt', encoding="UTF-8") as fobj:
            for ln in fobj.readlines():
                ln = ln.strip()
                #logd(ln)
                self.hack_file(ln)

def main():
    ''' main '''
    Solution.run()

if __name__=="__main__":
    main()
