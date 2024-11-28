#!/usr/bin/env python3
# coding: utf-8

'''
class variables
object variables
'''

class MyClass:
    ''' sample class '''
    my_class_variable = 10

    def __init__(self, x):
        self.x = x

    @classmethod
    def from_input_string(cls, input_string):
        ''' from input string '''
        x = int(input_string)
        return cls(x)

    @classmethod
    def get_my_class_variable(cls):
        ''' get class variable '''
        return cls.my_class_variable

def main():
    ''' main '''
    my_object = MyClass(5)
    new_object = MyClass.from_input_string('10')
    class_variable = MyClass.get_my_class_variable()

    print(my_object.x)  # Output: 5
    print(new_object.x)  # Output: 10
    print(class_variable)  # Output: 10

if __name__ == '__main__':
    main()
