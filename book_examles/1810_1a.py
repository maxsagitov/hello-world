from tkinter import *
import random
root = Tk()
canv = Canvas(root, height = 500, width = 500)
canv.pack()
x_change = 0
y_change = 1

def move():
    root.move(canv, x_change, y_change)

def main():
    move()
    root.after(50, main)

for n in range(10):
    x = random.randint(100, 400)
    y = random.randint(100, 400)
    cx = random.randint(40, 80)
    cy = random.randint(15, 30)
    obj = canv.create_polygon([x, y], [x+cx, y-cy], [x+cx, y+cy],
                              [x-cx, y-cy], [x-cx, y+cy], fill = 'black')
main()



root.mainloop()
