def create(name, var):
    d.update({name:{'parent':var,'vars':[]}})
    #print(d)
    
def add(name, var):
    d1 = d.get(name)
    #print(d1)
    l1 = d1['vars']
    #print (l1)
    l1.append(var)
    #print(d)

def get(name, var):
    d1 = d.get(name)
    #print(d1)
    l1 = d1['vars']
    #print(l1)
    if var in l1:
        return name
    elif d1['parent'] != 'None':
        return get(d1['parent'], var)
    else:
        return 'None'

d = {'global':{'parent':'None','vars':[]}}
n = int(input())
if n>=1 and n<=100:
    for i in range(n):
        cmd, namesp, arg = input().split()
    #print(cmd, namesp, arg)
        if cmd == "create":
            create(namesp, arg)
        if cmd == "add":
            add(namesp, arg)
        if cmd == "get":
            p = get(namesp, arg)
            print(p)
