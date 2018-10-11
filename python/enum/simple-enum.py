''' simple enum '''

from __future__ import print_function
from enum import Enum

class Fruit(Enum):
    apple = 1
    banana = 2
    orange = 3

print('list all fruits:')
for ff in Fruit:
    print(ff, '=', ff.value)

print()
print('Fruit.apple: {}'.format(Fruit.apple))
print('Fruit(2): {}'.format(Fruit(2)))
print('Fruit.orange.value: {}'.format(Fruit.orange.value))
