import field
import snake
import tkinter as tk


# mai part
win = field.field()
win.render()
player = snake.Snake(win)
player.respawn(win.field[8][4], win.field[8][5], win.field[8][6])
win.win.bind('<w>', lambda event: player.change_vektor([-1, 0]))
win.win.bind('<a>', lambda event: player.change_vektor([0, -1]))
win.win.bind('<s>', lambda event: player.change_vektor([1, 0]))
win.win.bind('<d>', lambda event: player.change_vektor([0, 1]))

a = ''
def time():
    a = win.win.after(250, time)
    temp = player.move()
    if temp == False:
        print(1)
        win.win.after_cancel(a)

win.spawn_food()
time()
#end of main part

win.puplic()


print(win.field)