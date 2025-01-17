'''
python module as a config file
'''

import sys

digests = [
    {
        "cmd": "/usr/bin/md5sum",
        "func": "md5sum",
        "hash": "md5"
    },
    {
        "cmd": "/usr/bin/sha512sum",
        "func": "sha512sum",
        "hash": "sha512"
    },
    {
        "cmd": "/usr/bin/openssl dgst -sha3-256 ",
        "func": "sha3_256sum",
        "hash": "sha3_256"
    },
    {
        "cmd": "/usr/bin/openssl dgst -sha3-512 ",
        "func": "sha3_512sum",
        "hash": "sha3_512"
    },
]

if __name__ == "__main__":
    print('not a standalone script, exit...')
    sys.exit(1)
