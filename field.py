import tkinter as tk
from random import randint


class chank(tk.Button):
    #normal chank
    def __init__(self, master, x=0, y=0, *args, **kwargs):
        super(chank, self).__init__(master, *args, **kwargs)
        self.cord = [x, y]
        self.colour = None
        self.colision = True

    def __repr__(self):
        return f'{self.cord, self.colision}'
    def __str__(self):
        return f'{self.cord, self.colour, self.colision}'

class field:
    max_x = 20
    max_y = 20
    win = tk.Tk()

    def __init__(self):
        self.field = []
        for i in range(field.max_x):
            row = []
            for j in range(field.max_y):
                btn = chank(field.win, x=i, y=j, width=3, background='black', relief='flat', state = 'disabled', text='#')
                row.append(btn)
            self.field.append(row)

    def render(self):
        for i in range(field.max_x):
            for j in range(field.max_y):
                if 0 in self.field[i][j].cord or 19 in self.field[i][j].cord:
                    continue
                else:
                    self.field[i][j].colision = False
                    self.field[i][j].config(text = '')
                    self.field[i][j].grid(row=i, column=j)
                #print(i, j)
    

    # spawning food
    def spawn_food(self):
        x = randint(1, field.max_x - 1)
        y = randint(1, field.max_y - 1)
        if self.field[x][y].colision == True:
            x1 = x
            y1 = y
            while self.field[x1][y1].colision == True:
                print(x1, y1, self.field[x1][y1].colision)
                if x1 >= field.max_x - 1:
                    x1 = 1
                    y1 += 1
                else:
                    x1 += 1
                if y1 >= field.max_y - 1:
                    y1 = 1
            
            return self.food(self.field[x1][y1])
        else:
            print(x,y, self.field[x][y].colision)
            return self.food(self.field[x][y])
    
    def food(self, part: chank):
        part['background'] = 'blue'
        return part


        
    # ending of spawning food

    def puplic(self):
        field.win.mainloop()