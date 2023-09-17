#!/usr/bin/env python3
# coding: utf-8
#

'''
part of 37k
part of 71k
'''

class Solution():
    PART = [(0,1,2), (0,1,3), (0,1,4), (1,2,3), (1,2,4), (2,3,4)]

    def init(self):
        pass

    @staticmethod
    def get_part(v):
        parts = []
        t = []
        for p in Solution.PART:
            t = [v[p[0]], v[p[1]], v[p[2]]]
            i = [p[0], p[1], p[2]]
            parts.append((t, i))
        return parts

    @staticmethod
    def is_inrange(n):
        return 10<=n<=99

    @staticmethod
    def isparts37(parts):
        for (t, i) in parts:
            if sum(t) % 37 == 0:
                return (t, i)
        return None

    def isparts71(parts):
        for (t, i) in parts:
            if sum(t) % 71 == 0:
                return (t, i)
        return None

    @staticmethod
    def get_values(start):
        vals = []
        t = start
        for i in range(5):
            if Solution.is_inrange(t):
                vals.append(t)
                t += 1
            else:
                raise ValueError
        return vals

    @staticmethod
    def show(msg, klist):
        print(msg)
        for (t, i) in klist:
            s = sum(i[0])
            print(f'{t=},{i=},{s=}')
            #(n, r) = k
            #print(n, r, sum(r))

    def action(self):
        ''' action '''
        print('action!')
        k37=[]
        k71=[]
        try:
            for i in range(10,99):
                n = Solution.get_values(i)
                parts = Solution.get_part(n)
                ret = Solution.isparts37(parts)
                if ret:
                    #print(f'seq:{n}, part:{ret}, is 37k')
                    k37.append((n, ret))
                ret = Solution.isparts71(parts)
                if ret:
                    #print(f'seq:{n}, part:{ret}, is 71k')
                    k71.append((n, ret))
        except ValueError:
            pass

        Solution.show("k37", k37)
        Solution.show("k71", k71)


    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

def main() -> None:
    ''' main '''
    print(__doc__)
    Solution.run()

if __name__ == '__main__':
    main()
