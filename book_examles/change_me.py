# -*- coding: cp1251 -*-
def new():
    l1 = [line.replace('’',"'") for line in open('temp.txt')]
    result1 = open('temp.txt', 'w')
    for i in l1:
        result1.write(i)
    print('THERE1')
    result1.close()    
    l2 = [line.replace('‘',"'") for line in open('temp.txt')]
    result2 = open('temp.txt', 'w')
    for i in l2:
        result2.write(i)
    result2.close()
    l3 = [line.replace('“','"') for line in open('temp.txt')]
    result3 = open('temp.txt', 'w')
    for i in l3:
        result3.write(i)
    result3.close()
    l4 = [line.replace('”','"') for line in open('temp.txt')]
    result4 = open('temp.txt', 'w')
    for i in l4:
        result4.write(i)
    result4.close()
new()

