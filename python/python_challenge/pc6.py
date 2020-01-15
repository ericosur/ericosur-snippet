#!/usr/bin/python

'''
python challenge level 6
'''

import re
import zipfile

def main():
    ''' main '''
    zfile = 'ch.zip'
    start = '90052'
    history = []

    zfile = zipfile.ZipFile(zfile, 'r')

    idx = start
    while True:
        data = zfile.read(idx + '.txt')
        m = re.search(r'(\d+)', str(data))
        if m:
            idx = m.group(1)
            #print(idx)
            history.append(idx)
        else:
            break

    msg = ''
    for i in history:
        cmt = zfile.getinfo(i + '.txt').comment
        msg = msg + cmt.decode()

    print(msg)
    '''
    print(''.join([zfile.getinfo(i+'.txt').comment for i in history]))
    '''
    zfile.close()
    # oxygen

if __name__ == '__main__':
    main()
