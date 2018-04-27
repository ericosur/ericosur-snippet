'''
* prepare a file list eg list.txt
* python file-input-sample.py list.txt
  * will output each line of list.txt

* may think it as a opened file and list each list of it
  * it could handle '-' as stdin
'''

import fileinput

for line in fileinput.input():
    line = line.strip()
    print(line)
