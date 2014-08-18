from factorial_exponent_plot import load_pickle, save_pickle, get_factorial

from math import exp, sqrt, pi, log

def est_fib(m):
    '''
    reference from:
    http://zh.wikipedia.org/zh-tw/%E9%9A%8E%E4%B9%98
    '''
    _lower = 1.0/(12.0*m+1.0)
    _upper = 1.0/(12.0*m)
    _avg = (_lower + _upper) / 2.0
    ans = sqrt(2.0*pi*m) * (m/exp(1.0))**m * exp(_avg)
    return ans

if __name__ == '__main__':
    load_pickle()

    NUMBER = 170    # the max number est_fib() could calculate

    real = get_factorial(NUMBER)
    print("real = ", log(real))
    est = est_fib(NUMBER)
    print("est = ", log(est))

    save_pickle()
