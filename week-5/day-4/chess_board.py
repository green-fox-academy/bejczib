from tkinter import *

master = Tk()

w = Canvas(master, width = 400, height = 400)

w.pack()

# table = 1
# while table <= 8:
#     j = 20
#     for i in range(j, 180, 40):
#         w.create_rectangle(i+20, 0, i+40, 20, fill = '#ff0000')
#
#     for i in range(j, 180, 40):
#         w.create_rectangle(i, 20, i+20, 40, fill = '#ff0000')
#     j += 20
#     table +=1


# w.create_rectangle(20, 0, 40, 20, fill = '#ff0000')
# w.create_rectangle(60, 0, 80, 20, fill = '#ff0000')
# w.create_rectangle(100, 0, 120, 20, fill = '#ff0000')
# w.create_rectangle(140, 0, 160, 20, fill = '#ff0000')
#
# w.create_rectangle(40, 20, 60, 40, fill = '#ff0000')
# w.create_rectangle(80, 20, 100, 40, fill = '#ff0000')
# w.create_rectangle(120, 20, 140, 40, fill = '#ff0000')
# w.create_rectangle(160, 20, 180, 40, fill = '#ff0000')
#
# w.create_rectangle(20, 40, 40, 60, fill = '#ff0000')
# w.create_rectangle(60, 40, 80, 60, fill = '#ff0000')
# w.create_rectangle(100, 40, 120, 60, fill = '#ff0000')
# w.create_rectangle(140, 40, 160, 60, fill = '#ff0000')

j = 0
while j <=140:
    for i in range(0,160,40):
        w.create_rectangle(i+20, j, i+40, j+20, fill = '#ff0000')
    for i in range(0,160,40):
        w.create_rectangle(i+40, j+20, i+60, j+40, fill = '#ff0000')
    j += 40

mainloop()
