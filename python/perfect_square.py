#!/usr/bin/env python
#

start = 31
end = 99

x = start
cnt = 0
while ( x <= end):
    print '{0:2d}    {1:4d}'.format(x, x*x)
    x = x + 1
    cnt = cnt + 1

print("cnt:", cnt)

