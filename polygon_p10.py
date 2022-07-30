from turtle import *

pencolor('blue')
pensize(3)
speed('slowest')
for i in range(4):
    pencolor('red')
    forward(100)
    for i in range (6):
        forward(100)
        pencolor('black')
        write(i,font=('Arial',14,'normal'),align='left')
        left(360/6)
    left(360/4)

mainloop()
