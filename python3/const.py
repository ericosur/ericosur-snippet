#!/usr/bin/python3
# coding: utf-8

'''
demo of const variable in python

reference: http://web.archive.org/web/20100523132518/http://code.activestate.com/recipes/65207-constants-in-python/?in=user-97991

'''

# Put in const.py...:
class _const():
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise TypeError("Can't rebind a const: {}".format(name))
        self.__dict__[name] = value

import sys
sys.modules[__name__]=_const()

def main():
    ''' demo '''

    # that's all -- now any client-code can
    import const
    # and bind an attribute ONCE:
    const.magic = 23
    # but NOT re-bind it:
    const.magic = 88      # raises const.ConstError
    # you may also want to add the obvious __delattr__

if __name__ == '__main__':
    main()
