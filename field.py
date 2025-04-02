import tkinter as tk

class chank(tk.Button):
    def __init__(self, master, x=0, y=0, *args, **kwargs):
        super(chank, self).__init__(master, *args, **kwargs)
        self.cord = [x, y]
        self.colour = 'white'
        self.colision = True
    
    def __repr__(self):
        return f'{self.cord, self.colour, self.colision}'
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

    def render(self):                                       # <-----------Problem (list index out of rabge)
        for i in range(field.max_x):
            for j in range(field.max_y):
                if 0 in self.field[i][j].cord:
                    continue
                else:
                    self.field[i][j].colision = False
                    self.field[i][j].config(text = '')
                    self.field[i][j].grid(row=i, column=j)
                print(i, j)
        
    def puplic(self):
        field.win.mainloop()