n = int(input())
graph = {}
while n > 0:
    n -= 1
    class_attr = input().split()
"""    print(class_attr)
    graph[class_attr[0]] = class_attr[2:]
"""
    for i in class_attr[2:]:
        graph[i].add(class_attr[0])
        
print(graph)

def find_err(err):
    for i in graph[err]:
        if 
        





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
