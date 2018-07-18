import sys, mytimer   
reps = 10000
repslist = range(reps)
from math import sqrt
def mathMod():
    #res = []
    for x in repslist:
        #res.append(abs(x))
        res = sqrt(x)
    return res
def powCall():
    #res = []
    for x in repslist:
        #res.append(abs(x))
        res = pow(x, .5)
    return res
def powExpr():
    #res = []
    for x in repslist:
        #res.append(abs(x))
        res = x**.5
    return res
#def listComp():
#    return [sqrt(x) for x in repslist]
"""def mapCall():
    return list(map(abs, repslist))   
def genExpr():
    return list(abs(x) for x in repslist) 
def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())
print(sys.version)"""
for tester in (mytimer.timer, mytimer.best):
    print('<%s>' % tester.__name__)
    for test in (powCall, mathMod, powExpr):
        elapsed, result = tester(test)
    #elapsed, result = mytimer.timer(test)
        print ('-' * 33)
        print ('%-9s: %.5f => [%s]' %
            (test.__name__, elapsed, result))
