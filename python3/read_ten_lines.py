#!python3
# coding: utf-8
#

'''
不知道為什麼，從 mac 端推上去的檔案，python script讀不到，
現在土炮的解法是，用這個 script 產生一個檔案，在 mac 把內容
cat 過去，這樣就能讀到內容了。
'''


fn = 'prime.txt'

with open(fn, 'rt', encoding='utf-8') as fin:
    cnt = 0
    for ln in fin.readlines():
        cnt += 1
        if cnt > 10:
            break
        print(ln.strip())
