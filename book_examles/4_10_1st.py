import random, math
from tkinter import Tk, Canvas
canvas_size = 500
colors = ["red","orange","yellow","green","blue","cyan","magenta","light blue"]
root = Tk()
canv = Canvas(root, width=500,height=500,bg="lightblue") #создаём объект-холст
canv.pack() #разместим на главном окне
npoints = 5

x = []

y = []

for i in range(npoints):

    x.append(random.randint(0, canvas_size))

    y.append(random.randint(0, canvas_size))

for i in range(npoints):

        for j in range(i + 1, npoints):

            color = random.choice(colors)

            canv.create_line(x[i], y[i], x[j], y[j], fill = color, width = 2)
"""alpha = 0

x_start = canvas_size/2

y_start = 100

x1 = x_start

y1 = y_start

betha = random.randint(50, 90)

for i in range (200):

    size = 100

    alpha = (alpha + betha) % 360

    x2 = x1 + size * math.cos(math.radians(alpha))

    y2 = y1 + size * math.sin(math.radians(alpha))

    color = random.choice(colors)

    canv.create_line(x1,y1,x2,y2, fill=color, width=2)

    x1 = x2

    y1 = y2

    if (int (x2-x_start) == 0)&(int (y2-y_start) == 0):

        break

r = 1

x = r

y = canvas_size/2

color = "blue"
i = 0
while (x < canvas_size - r):
    if i % 2 == 0:

        color = "blue"

    else:

        color = "red"
    i += 1

    canv.create_oval(x - r, y - r, x + r, y + r, fill = color)

    x += r

    r +=1

    x += r
for i in range(10):

    size = random.randint(1,canvas_size/2)

    x=random.randint(0, canvas_size-size)

    y=random.randint(0, canvas_size-size)

    color = random.choice(colors)

    print (x,y,size)

    canv.create_oval(x,y,x+size,y+size, fill=color, width=0)    
"""
root.mainloop()
