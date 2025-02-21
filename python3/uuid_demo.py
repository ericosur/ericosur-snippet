#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
'''
uuid demo
from: https://docs.python.org/2/library/uuid.html
'''

import uuid

def sep() -> None:
    ''' separator'''
    print('-' * 45)

def main():
    ''' main test function '''
    sep()
    for _ in range(2):
        # uuid1: host id and current time
        print(f"uuid1: {uuid.uuid1()}")
        # uuid3: md5 hash namespace and a name
        uid3 = uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')
        print(f"uuid3: {uid3}")
        # uuid4: random uuid
        print(f"uuid4: {uuid.uuid4()}")
        # uuid5: sha1 hash namespace and a name
        uid5 = uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')
        print(f"uuid5: {uid5}")
        sep()

if __name__ == "__main__":
    main()
