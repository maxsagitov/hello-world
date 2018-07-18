"""import time
reps = 1000
repslist = range(reps)
def timer(func, *pargs, **kargs):
    start = time.clock()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = time.clock() - start
    return (elapsed, ret)
"""
import time, sys
if sys.platform[:3] == 'win':
    timefunc = time.clock            # В Windows использовать time.clock
else:
    timefunc = time.time             # На некоторых платформах Unix дает
                                        # лучшее разрешение
#def trace(*args): pass               # Заглушка: вывод аргументов
trace = lambda *args: None
def timer(func, *pargs, _reps=1000, **kargs):
    trace(func, pargs, kargs, _reps)
    start = timefunc()
    for i in range(_reps):
        ret = func(*pargs, **kargs)
    elapsed = timefunc() - start
    return (elapsed, ret)
"""def timer(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 1000) # Полученное число повторов
                                        # или значение по умолчанию
    trace(func, pargs, kargs, _reps)
    repslist = range(_reps)          # Вызов range вынесен за пределы
                                        # цикла for для версии 2.6
    start = timefunc()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timefunc() - start
    return (elapsed, ret)"""
def best(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 50)
    best = 2 ** 32
    for i in range(_reps):
        (time, ret) = timer(func, *pargs, _reps=1, **kargs)
        if time < best: best = time
    return (best, ret)
