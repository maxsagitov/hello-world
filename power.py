L = [1, 2, 4, 8, 16, 32, 64]
X = 5
for i in L:
    if 2 ** X == i: print('at index', L.index(i)); break    
else:
    print(X, 'not found')

for c in range(10):
    L.append(2**c)
print(L)

if 2**X in L:
    print('at index', L.index(2**X))
