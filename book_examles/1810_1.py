from tkinter import *
import random
root = Tk()
canv = Canvas(root, height = 500, width = 500)
canv.pack()

def string():
    canv.create_polygon([x, y], [x+cx, y-cy], [x+cx, y+cy], [x-cx, y-cy], [x-cx, y+cy], fill = 'black')
def string_w(x, y):
    canv.create_polygon([x, y], [x+cx, y-cy], [x+cx, y+cy], [x-cx, y-cy], [x-cx, y+cy], fill = 'wight')
def step():
    global x, y
    x += random.randinit(-5, 5)
    y += (-1)
lx = ly = lcx = lcy = []
i = True
while True:
    if i == True:
        for n in range(10):
            x = random.randint(100, 400)
            lx.append(x)
            y = random.randint(100, 400)
            ly.append(y)
            cx = random.randint(40, 80)
            lcx.append(cx)
            cy = random.randint(15, 30)
            lcy.append(cy)
            string()
        break
'''    else:
        if i == True:
            pass
        else:
            for n in range(10):
                string_w()
'''            
        
        
root.mainloop()

