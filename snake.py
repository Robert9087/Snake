from collections import deque
from field import chank

class Snake:
    length = deque()
    right_vektor = [1, 0]
    left_vektor = [-1, 0]
    bottom_vektor = [0, 1]
    upper_vektor = [0, -1]
    current_vektor = right_vektor

    def __init__(self, field:list):
        self.field = field



    def respawn(self, one: chank, two: chank, third: chank):
        Snake.length.append([self.body(one), self.body(two), self.body(third)])
    
    def move(self):
        head = Snake.length[2]
        next = self.field[head.cord[0] + Snake.current_vektor[0]][head.cord[1] + Snake.current_vektor[1]]
        if next.colision == True:
            return False
        else:
            Snake.length.append(self.body(next))
            tail = Snake.length.popleft()
            self.body(tail)
        

    def change_vektor(self, dir):
        return
    
    def time(self):
        return
    
    def body(self, part: chank):
        if part.colision == True:
            part['background'] = 'red'
            part.colision = False
        else:
            part['background'] = 'black'
            part.colision = True
        return part