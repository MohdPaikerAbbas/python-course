from turtle import *

pencolor('blue')
pensize(3)
speed('fastest')
for i in range(6):
    pencolor('red')
    forward(100)
    for i in range (6):
        circle(20)
        forward(100)
        pencolor('black')
        left(360/6)
    left(360/6)

mainloop()
