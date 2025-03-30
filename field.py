import tkinter as tk

class chank(tk.Button):
    def __init__(self, master, x=0, y=0, *args, **kwargs):
        super(chank, self).__init__(master, *args, **kwargs)
        self.cord = [x, y]
        self.colour = 'white'
        self.colision = True
    
    def __repr__(self):
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
                btn = chank(field.win, x=i, y=j, width=3, background='black', relief='flat', state = 'disabled')
                row.append(btn)
            self.field.append(row)

    def render(self):
        for i in range(1, field.max_x - 1):
            for j in range(1, field.max_y - 1):
                self.field[i][j].grid(row=i, column=j)
                self.field[i][j].colision = False
        
        field.win.mainloop()