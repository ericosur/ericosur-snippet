
'''
from: https://tools.ietf.org/html/rfc7914#section-12

   scrypt (P="", S="", N=16, r=1, p=1, dklen=64) =
   77 d6 57 62 38 65 7b 20 3b 19 ca 42 c1 8a 04 97
   f1 6b 48 44 e3 07 4a e8 df df fa 3f ed e2 14 42
   fc d0 06 9d ed 09 48 f8 32 6a 75 3a 0f c8 1f 17
   e8 d3 e0 fb 2e 0d 36 28 cf 35 e2 0c 38 d1 89 06

   scrypt (P="password", S="NaCl", N=1024, r=8, p=16, dkLen=64) =
   fd ba be 1c 9d 34 72 00 78 56 e7 19 0d 01 e9 fe
   7c 6a d7 cb c8 23 78 30 e7 73 76 63 4b 37 31 62
   2e af 30 d9 2e 22 a3 88 6f f1 09 27 9d 98 30 da
   c7 27 af b9 4a 83 ee 6d 83 60 cb df a2 cc 06 40

   scrypt (P="pleaseletmein", S="SodiumChloride", N=16384, r=8, p=1, dkLen=64) =
   70 23 bd cb 3a fd 73 48 46 1c 06 cd 81 fd 38 eb
   fd a8 fb ba 90 4f 8e 3e a9 b5 43 f6 54 5d a1 f2
   d5 43 29 55 61 3f 0f cf 62 d4 97 05 24 2a 9a f9
   e6 1e 85 dc 0d 65 1e 40 df cf 01 7b 45 57 58 87

   scrypt (P="pleaseletmein", S="SodiumChloride", N=1048576, r=8, p=1, dkLen=64) =
   21 01 cb 9b 6a 51 1a ae ad db be 09 cf 70 f8 81
   ec 56 8d 57 4a 2f fd 4d ab e5 ee 98 20 ad aa 47
   8e 56 fd 8f 4b a5 d0 9f fa 1c 6d 92 7c 40 f4 c3
   37 30 40 49 e8 a9 52 fb cb f4 5c 6f a7 7a 41 a4
'''

from hashlib import scrypt
from pydantic import BaseModel

def show_hex(dk: bytes) -> None:
    ''' show hex in 16 bytes one line '''
    hex_str = dk.hex()
    for i in range(0, len(hex_str), 32):
        print(hex_str[i:i+32])
    print()

class ScryptVector(BaseModel):
    ''' vectors '''
    P: str
    S: str
    N: int
    r: int
    p: int
    dklen: int

def do_scrypt(pwd: bytes, salt: bytes) -> dict:
    ''' call hashlib.scrypt '''
    raw_dict = {}
    dk = scrypt(password=pwd, salt=salt,
                        n=16384, r=8, p=1, dklen=64)
    raw_dict["salt"] = salt  # bytes
    raw_dict["dk"] = dk      # bytes
    return raw_dict

def run_test_vector(arg: ScryptVector) -> None:
    '''
    run test vector
    '''
    dk = genkey_vector(arg)
    show_hex(dk)

def genkey_vector(arg: ScryptVector) -> bytes:
    '''
    derive key from ScryptVector
    '''
    dk = b''
    try:
        p = arg.P.encode()
        s = arg.S.encode()
        dk = scrypt(password=p, salt=s,
                    n=arg.N, r=arg.r, p=arg.p, dklen=arg.dklen)
    except ValueError as err:
        print(f'error: {err}')
    return dk

if __name__ == "__main__":
    print("run_vectory.py provides functions for scrypt_demo.py")
