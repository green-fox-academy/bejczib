from tkinter import *

master = Tk()

w = Canvas(master, width = 400, height = 400)

w.pack()

# basic exercise
#----------------------
#
# w.create_line(10, 10, 10, 180, fill = '#000')
# w.create_line(10, 180, 180, 180, fill = '#000')
#
# i=180
# while i !=10:
#     w.create_line(10,i, i-10, 180)
#     i-=10



w.create_line(120,20, 120, 220, fill = '#000')
w.create_line(20,120,220,120, fill = '#000')


i = 120
while i !=10:
    w.create_line(120,i-10, i+100, 120)
    i -= 10

i = 120
while i!= 10:
    w.create_line(i-10,120, 120, 130-i)
    i-=10

i = 120
while i != 10:
    w.create_line(120,i + 100, i-10, 120)
    i-=10

i = 220
while i != 120:
    w.create_line(120,i, 350-i, 120)
    i -= 10





mainloop()
