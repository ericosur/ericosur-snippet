#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=too-many-instance-attributes
# pylint: disable=invalid-name

'''
simulate traffic lights
'''

class Traffic():
    ''' class to find solution '''
    def __init__(self):
        (self.at, self.bt, self.ct) = (40, 50, 60)
        (self.As, self.Bs, self.Cs) = (True, True, True)
        self.changed = False
        self.t = 0

    @staticmethod
    def gr(YesNo):
        ''' return G or R '''
        if YesNo:
            return "G"
        return "R"

    @staticmethod
    def rep(t, msg, YesNo):
        ''' print prev and current status '''
        fr = Traffic.gr(not YesNo)
        to = Traffic.gr(YesNo)
        print(f'{t}: {msg} {fr} => {to}', end=' ')

    def report(self):
        ''' report '''
        lights = [Traffic.gr(self.As), Traffic.gr(self.Bs), Traffic.gr(self.Cs)]
        if self.As and self.Bs and self.Cs:
            print(f'{self.t}: {lights} ========>>>')
        else:
            print()

    def dec(self):
        ''' decrease '''
        any_chang = 0
        self.at -= 1
        if self.at <= 0:
            any_chang += 1
            self.at = 40
            self.As = not self.As
            self.rep(self.t, "Light#A", self.As)

        self.bt -= 1
        if self.bt <= 0:
            any_chang += 1
            self.bt = 50
            self.Bs = not self.Bs
            self.rep(self.t, "Light#B", self.Bs)

        self.ct -= 1
        if self.ct <= 0:
            any_chang += 1
            self.ct = 60
            self.Cs = not self.Cs
            self.rep(self.t, "Light#C", self.Cs)

        if any_chang > 0:
            self.report()

    def action(self):
        ''' action '''
        for t in range(60*10):
            self.t = t
            self.dec()

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()


def main():
    ''' main '''
    Traffic.run()

if __name__ == '__main__':
    main()
