#file = open('README.txt')
def countLines(file):
#    i = 0
  #  for line in open(file):
 #       i += 1
#    return i
    name = open(file)
    return len(name.readlines())

def countChars(file):
    input = open(file)
    all = input.read()
    return len(all)

def test(file):
    print (countLines(file))
    print (countChars(file))


if __name__ == '__main__':
    print(test('mymod.py'))
