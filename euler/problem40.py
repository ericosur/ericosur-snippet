# -*- coding: utf-8 -*-
"""
@author: neo
"""
d=''
i=1
while len(d)<1000002:
    d=d+str(i)
    i+=1
print int(d[0])*int(d[9])*int(d[99])*int(d[999])*\
        int(d[9999])*int(d[99999])*int(d[999999])
