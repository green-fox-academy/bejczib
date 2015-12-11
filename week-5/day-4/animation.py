from tkinter import *

master = Tk()
canvas = Canvas(master, width = 300, height = 300)
canvas.pack()
x0 = 10
y0 = 30
x1 = 30
y1 = 50
color = 'red'
dx = 2
dy = 3
def move_line_left(event):
    canvas.move(bar,-20,0)

def move_line_right(event):
    canvas.move(bar,20,0)

ball = canvas.create_oval(x0,y0,x1,y1, fill = color)
bar = canvas.create_line(100, 270, 200, 270, fill = color)
while True:
    canvas.move(ball,dx,dy)
    canvas.after(20)
    canvas.update()
    x0_coord_ball = canvas.coords(ball)[0]
    y0_coord_ball = canvas.coords(ball)[1]
    x0_coord_bar = canvas.coords(bar)[0]
    x1_coord_bar = canvas.coords(bar)[2]
    canvas.bind("<Left>", move_line_left)
    canvas.bind("<Right>", move_line_right)
    canvas.focus_set()
    if  x0_coord_ball >= 280 or x0_coord_ball <= 0:
        dx *=-1
    if y0_coord_ball <=0:
        dy *= -1
    if y0_coord_ball >=250:
        if x0_coord_bar < x0_coord_ball < x1_coord_bar:
            dy *= -1
mainloop()
