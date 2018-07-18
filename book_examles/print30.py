import sys
def print30(*args, **kargs):
    sep = kargs.get('sep', ' ')        # Именованные аргументы
    end = kargs.get('end', '\n')       # со значениями по умолчанию
    file = kargs.get('file', sys.stdout)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)
