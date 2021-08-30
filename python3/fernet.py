#!/usr/bin/python3
# coding: utf-8
#
'''
demo of cryptography.fernet to encrypt/decrypt a text

https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/

'''

from cryptography.fernet import Fernet

def main():
    # we will be encryting the below string.
    message = "hello geeks"

    # generate a key for encryptio and decryption
    # You can use fernet to generate
    # the key or use random key generator
    # here I'm using fernet to generate key
    key = Fernet.generate_key()

    # Instance the Fernet class with the key
    fernet = Fernet(key)

    # then use the Fernet class instance
    # to encrypt the string string must must
    # be encoded to byte string before encryption
    encMessage = fernet.encrypt(message.encode())

    print("key:", key)
    print("original string: ", message)
    print("encrypted string: ", encMessage)

    # decrypt the encrypted string with the
    # Fernet instance of the key,
    # that was used for encrypting the string
    # encoded byte string is returned by decrypt method,
    # so decode it to string with decode methos
    decMessage = fernet.decrypt(encMessage).decode()
    print("decrypted string: ", decMessage)

if __name__ == '__main__':
    print(__doc__)
    main()
