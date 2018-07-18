from tkinter import *
 
# глобальные переменные
# настройки окна
WIDTH = 900
HEIGHT = 300
 
# настройки ракеток
 
# ширина ракетки
PAD_W = 10
# высота ракетки
PAD_H = 100
 
# настройки мяча
 
# радиус мяча
BALL_RADIUS = 30
 
# устанавливаем окно
root = Tk()
root.title("PythonicWay Pong")
 
# область анимации
c = Canvas(root, width=WIDTH, height=HEIGHT, background="#003300")
c.pack()
 
# элементы игрового поля
 
# левая линия
c.create_line(PAD_W, 0, PAD_W, HEIGHT, fill="white")
# правая линия
c.create_line(WIDTH-PAD_W, 0, WIDTH-PAD_W, HEIGHT, fill="white")
# центральная линия
c.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, fill="white")
 
# установка игровых объектов
 
# создаем мяч
BALL = c.create_oval(WIDTH/2-BALL_RADIUS/2,
                     HEIGHT/2-BALL_RADIUS/2,
                     WIDTH/2+BALL_RADIUS/2,
                     HEIGHT/2+BALL_RADIUS/2, fill="white")
 
# левая ракетка
LEFT_PAD = c.create_line(PAD_W/2, 0, PAD_W/2, PAD_H, width=PAD_W, fill="yellow")
 
# правая ракетка
RIGHT_PAD = c.create_line(WIDTH-PAD_W/2, 0, WIDTH-PAD_W/2, 
                          PAD_H, width=PAD_W, fill="yellow")
 

BALL_X_CHANGE = 20
# по вертикали
BALL_Y_CHANGE = 0
 
def move_ball():
    c.move(BALL, BALL_X_CHANGE, BALL_Y_CHANGE)
 
def main():
    move_ball()
    # вызываем саму себя каждые 30 миллисекунд
    root.after(30, main)
 
# запускаем движение
main()# запускаем работу окна
root.mainloop()

