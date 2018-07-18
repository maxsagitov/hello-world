import tkinter

import random

import math

canvas_size = 500

npoints = 5

colors = ["red","orange","yellow","green","blue","cyan","magenta","light blue"]

root=tkinter.Tk()

canv = tkinter.Canvas(root, width=canvas_size, height=canvas_size, bg="white")

canv.pack()

def draw():

    x = []

    y = []

    for i in range(npoints):

        x.append(random.randint(0, canvas_size))

        y.append(random.randint(0, canvas_size))

        canv.delete("all")

    for i in range(npoints):

        for j in range(i + 1, npoints):

            color = random.choice(colors)

            canv.create_line(x[i], y[i], x[j], y[j], fill = color, width = 2)

button = tkinter.Button(root, text='draw', width=30, command=draw)

button.pack()
