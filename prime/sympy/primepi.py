'''
demo primepi
'''

from sympy import nextprime, prevprime, prime, primepi

P=4_222_234_741

def test(n: int) -> None:
    ''' test '''
    # no of prime <= n
    no = primepi(n)
    print(f'primepi: {no}')

    print(f'prevprime: {prevprime(n)}')
    # nth prime
    ret = prime(no)
    assert ret == n
    print(f'prime: {prime(no)}')
    print(f'nextprime: {nextprime(n)}')

def show(n: int) -> None:
    ''' show n '''
    print(primepi(n))

def main():
    ''' main '''
    show(100)
    show(2**32)
    test(P)


if __name__ == '__main__':
    main()