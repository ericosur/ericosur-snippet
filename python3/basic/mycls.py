#!/usr/bin/python3
# coding: utf-8

class MyClass:
    my_class_variable = 10

    def __init__(self, x):
        self.x = x

    @classmethod
    def from_input_string(cls, input_string):
        x = int(input_string)
        return cls(x)

    @classmethod
    def get_my_class_variable(cls):
        return cls.my_class_variable

my_object = MyClass(5)
new_object = MyClass.from_input_string('10')
class_variable = MyClass.get_my_class_variable()

print(my_object.x)  # Output: 5
print(new_object.x)  # Output: 10
print(class_variable)  # Output: 10
