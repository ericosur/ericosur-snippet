#!/usr/bin/env python3
# coding; utf-8

'''
test class
'''

class TestBase():
    ''' test base '''
    tag = 'TestBase'

    def __str__(self):
        return f'{TestBase.tag}.__str__'

    def do_work(self):
        ''' do_work '''
        print('do_work =====>')
        self.work()

    def work(self):
        ''' work as a pure-virtual function '''
        raise NotImplementedError

class TestWork(TestBase):
    ''' test work '''
    tag = 'TestWork'

    def __init__(self, ll=1, uu=100):
        self.lower = ll
        self.upper = uu

    def work(self):
        ''' real work '''
        arr = list(range(self.lower, self.upper + 1))
        print(sum(arr))


def main():
    ''' main '''
    tp = TestWork()
    tp.do_work()
    tp.lower = 100
    tp.upper = 500
    tp.do_work()


if __name__ == '__main__':
    main()
