from turtle import *

pencolor('blue')
pensize(3)
speed('fastest')
for i in range(10):
    pencolor('red')
    forward(100)
    for j in range (8):
        pencolor('green')
        forward(50)
        for k in range (6):
            pencolor('purple')
            forward(25)
            left(360/6)
        left(360/8)
    left(360/10)        

mainloop()
