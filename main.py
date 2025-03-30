import field
import snake
import tkinter as tk

win = field.field()
player = snake.Snake(win.field)
player.respawn(win.field[8][4], win.field[8][5], win.field[8][6])




win.render()




print(win.field)