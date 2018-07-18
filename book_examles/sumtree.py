def sumtree(L):
    tot = 0
    for x in L:                # Обход элементов одного уровня
        if not isinstance(x, list):
            tot += x           # Числа суммируются непосредственно
        else:
            tot += sumtree(x)  # Списки обрабатываются рекурсивными вызовами
    return tot
L = [1, [2, [3, 4], 5], 6, [7, 8]] # Произвольная глубина вложения
print(sumtree(L))
