"""n = int(input())
graph = {}
while n > 0:
    n -= 1
    class_attr = input().split()
    print(class_attr)
    for i in class_attr[2:]:
        if i not in graph:
            graph[i] = {class_attr[0]}
        else:
            graph[i].add(class_attr[0])

print(graph)
"""
graph = {'6': ['5'], '9': ['8'], '2': ['1'], '5': ['5'], '4': ['5', '1'], '3': ['1'], '1': ['8']}

def foo(keys):
   # for keys in graph:
        print('key', keys)
        for i in graph[keys]:
            print('val',i)
            if i in graph.keys():
                print(i, graph[i])
                graph[keys].append(graph[i])
for i in graph:
    foo(i)
print(graph)
"""
print(graph)

def find_err(err):
    for i in graph[err]:
        pass
        





def find_it(parent, her):    
    if not parent in graph:
        return  print('No')
    try:
        if graph[parent] == graph[her]:
            return print ('Yes')
    
        
        for node in graph[her]:
            #print(node)
            if parent not in graph[her]:
                find_it(node, her)
                break
            return print('Yes')
        else:    
            return print('No')
    except Exception:
        print ('No')
             
#print (graph)

q = int(input())
while q > 0:
    q -= 1
    res = input().split()
    #print (res)
    find_it (res[0], res[1])
"""
