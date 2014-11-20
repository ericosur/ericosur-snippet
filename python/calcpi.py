#!/usr/bin/python

# c/p from http://snippets.dzone.com/posts/show/5433

import random, math

class calcPi:
    def __init__(self):
        self.times = pow(10,6)
        self.i = 0
        self.isnot = 0

    def IsOnCircle(self,x,y):
        if math.sqrt(x**2+y**2) < 1:
            return True
        else:
            return False

    def run(self):
        for x in range(self.times):
            x,y = random.random(),random.random()
            if self.IsOnCircle(x,y):
                self.i+=1
            else:
                self.isnot+=1

    def getResults(self):
        return (float(self.i), float(self.isnot))

    def getPi(self):
        self.run()
        r = self.getResults()
        return r[0]/(r[0]+r[1])*4

if __name__ == '__main__':
    print calcPi().getPi()
