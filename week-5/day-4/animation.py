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
def move_bar_bottom_left(event):
    canvas.move(bar_bottom,-20,0)

def move_bar_bottom_right(event):
    canvas.move(bar_bottom,20,0)

def move_bar_top_left(event):
    canvas.move(bar_top,-20,0)

def move_bar_top_right(event):
    canvas.move(bar_top,20,0)

ball = canvas.create_oval(x0,y0,x1,y1, fill = color)
bar_bottom = canvas.create_line(100, 270, 200, 270, fill = color)
bar_top = canvas.create_line(15, 15, 115, 15, fill = color)

while True:
    canvas.move(ball,dx,dy)
    canvas.after(20)
    canvas.update()
    x0_coord_ball = canvas.coords(ball)[0]
    y0_coord_ball = canvas.coords(ball)[1]
    x0_coord_bar_bottom = canvas.coords(bar_bottom)[0]
    x1_coord_bar_bottom = canvas.coords(bar_bottom)[2]
    x0_coord_bar_top = canvas.coords(bar_top)[0]
    x1_coord_bar_top = canvas.coords(bar_top)[2]
    canvas.bind("<Left>", move_bar_bottom_left)
    canvas.bind("<Right>", move_bar_bottom_right)
    canvas.bind("<a>", move_bar_top_left)
    canvas.bind("<d>", move_bar_top_right)
    canvas.focus_set()
    if  x0_coord_ball >= 280 or x0_coord_ball <= 0:
        dx *=-1
    # if y0_coord_ball <=0:
    #     dy *= -1
    if y0_coord_ball >=250:
        if x0_coord_bar_bottom < x0_coord_ball < x1_coord_bar_bottom:
            dy *= -1
    if y0_coord_ball <=30:
        if x0_coord_bar_top < x0_coord_ball < x1_coord_bar_top:
            dy *= -1

mainloop()
