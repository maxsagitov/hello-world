import random
pop = [1, 2, 3, 4, 5]
l1 = random.sample(pop, 5)
l2 = random.sample(pop, 5)
print(l1, l2)
num = 1
for i in range(len(l2)):
    l1.insert(num, l2[i])
    num += 2
print(l1)
