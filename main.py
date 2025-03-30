import field
import snake
import tkinter as tk



win = field.field()
player = snake.Snake(win.field)
player.respawn(win.field[8][4], win.field[8][5], win.field[8][6])
win.win.bind('<w>', lambda event: player.change_vektor('w'))
win.win.bind('<a>', lambda event: player.change_vektor('a'))
win.win.bind('<s>', lambda event: player.change_vektor('s'))
win.win.bind('<d>', lambda event: player.change_vektor('d'))



win.render()




print(win.field)