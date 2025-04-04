from collections import deque
from field import chank
from tkinter import Tk

class Snake:
    length = deque()
    right_vektor = [1, 0]
    left_vektor = [-1, 0]
    bottom_vektor = [0, 1]
    upper_vektor = [0, -1]
    current_vektor = [0, 1]

    def __init__(self, field):
        self.field = field.field
        self.root = field
        self.long = 3


    def respawn(self, one: chank, two: chank, third: chank):
        Snake.length.append(self.body(one))
        Snake.length.append(self.body(two))
        Snake.length.append(self.body(third))
    
    def move(self):
        #print(Snake.length)
        head = Snake.length[-1]
        #print(head)
        next = self.field[head.cord[0] + Snake.current_vektor[0]][head.cord[1] + Snake.current_vektor[1]]
        #print(next)
        if next.colision == True:
            return False
        elif next['background'] == 'blue':
            self.eat(next)
            return                          # <----- eat here
        else:
            Snake.length.append(self.body(next))
            tail = Snake.length[0]
            self.body(tail)
            Snake.length.popleft()
            return True
            
        

    def change_vektor(self, dir):
        if Snake.current_vektor == dir:
            print('stop')
            return
        temp = Snake.current_vektor
        a = [i * -1 for i in temp]
        if dir == a:
            return
        else:
            Snake.current_vektor = dir
    

    a = ''
    def time(root: Tk):
        return
    
    def body(self, part: chank):
        if part.colision == False:
            part['background'] = 'red'
            part.colision = True
        elif part.colision == True:
            part['background'] = 'black'
            part.colision = False
        return part
    

    def eat(self, part: chank):
        part['background'] = 'red'
        part.colision = True
        Snake.length.append(part)
        self.root.spawn_food()