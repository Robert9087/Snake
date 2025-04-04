'''from collections import deque
import keyboard

def check(event):
    print(event.name)

a = keyboard.on_press(check)


keyboard.wait('esc')'''


'''a = deque([1,2,3,4,5])
a.pop()
a.popleft()
print(a)

a = [1,2]
b = [1,1]

zip(a, b)

print(a) '''
from random import choice
l = [1,2,3,4,5,7,3]
print(choice(l))