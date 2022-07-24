from turtle import *

speed('slowest')
pencolor('white')
bgcolor('black')

side=45
size=10
for i in range(side):
    fd(size)
    lt(360/side)

mainloop()    