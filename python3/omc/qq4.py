#!/usr/bin/env python3

'''
Q4 把100分成兩個自然數的和，其中一個是7的倍數，另一個是11的倍數，
那麼這兩個自然數的乘積是多少
'''




def main():
    ''' main test function '''
    for x in range(1,55):
        for y in range(1, 55):
            for z in range(1, 55):
                if y==2*x and x+y+z==55:
                    print(x,y,z)



if __name__ == '__main__':
    main()
