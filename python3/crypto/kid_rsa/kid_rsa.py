''' module kidrsa

kid RSA
https://www.cs.uri.edu/cryptography/publickeykidkrypto.htm

'''

__version__ = '0.0.1'

# encryption C = P * e (mod n)
def encrypt(P, n, e):
    ''' encrypt '''
    C = (P * e) % n
    return C

# decryption P = C * d (mon n)
def decrypt(C, n, d):
    ''' decrypt '''
    P = (C * d) % n
    return P

def make_pair(a, b, a1, b1):
    ''' make pair '''
    M = a * b - 1
    e = (a1 * M) + a
    d = (b1 * M) + b
    n = ((e * d) - 1) // M
    return n, e, d, M

def main():
    ''' main '''
    print('This is module kid_rsa')

if __name__ == '__main__':
    main()
