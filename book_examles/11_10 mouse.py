import tkinter

import random

import math

canvas_size = 500

side = 20

radius = 50

root = tkinter.Tk()

canv = tkinter.Canvas(root, width=canvas_size, height=canvas_size, background='gray')

canv.pack(fill="both", expand="yes")

#canv.create_rectangle(0, 0, side, side, fill='blue')

def on_mouse_move(event):

    canv.delete("all")

    x = canv.canvasx(event.x)

    y = canv.canvasy(event.y)

    canv.create_rectangle(x, y, x + side, y + side, fill='blue')

def on_click(event):

    canv.delete("all")

    x = canv.canvasx(event.x)

    y = canv.canvasy(event.y)

    alpha = random.randint(0, 360)

    x = x + radius * math.cos(math.radians(alpha))

    y = y + radius * math.sin(math.radians(alpha))

    canv.create_rectangle(x, y, x + side, y + side, fill='blue')

canv.bind('<Motion>', on_mouse_move) #связать событие движения мыши на холсте с нашей функцией on_mouse_move

canv.bind('<ButtonPress>', on_click) #связать событие нажатия мыши на холсте с нашей функцией on_click

root.mainloop()
