import field
import snake
import tkinter as tk



win = field.field()
player = snake.Snake(win.field)
player.respawn(win.field[8][4], win.field[8][5], win.field[8][6])
win.win.bind('<w>', lambda event: player.change_vektor([-1, 0]))
win.win.bind('<a>', lambda event: player.change_vektor([0, -1]))
win.win.bind('<s>', lambda event: player.change_vektor([1, 0]))
win.win.bind('<d>', lambda event: player.change_vektor([0, 1]))



win.render()




#print(win.field)