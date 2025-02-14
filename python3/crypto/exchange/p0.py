'''
test from_env
'''

from keyiv import from_env

k = from_env("KEY", 32)
print("type of k:", type(k))
print('key:')
print(k)
print('len:', len(k))
print('key in hex:')
print(k.hex())
