#!/usr/bin/env python3

'''
netflix series GNOSIA, one character is called SQ
count from A to Z, then AA to AZ, then BA to BZ, and so on until SQ
'''

def main():
    ''' main '''
    cnt = 0
    for i in range(26):
        #print(chr(ord('A') + i))
        cnt += 1
    for i in range(26):
        for j in range(26):
            the_name = chr(ord('A') + i) + chr(ord('A') + j)
            cnt += 1
            if the_name == 'SQ':
                print(f'name: {the_name} and count is {cnt}')
                break


if __name__ == '__main__':
    main()
