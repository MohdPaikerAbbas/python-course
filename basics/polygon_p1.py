from turtle import *

speed('slowest')
pencolor('white')
bgcolor('black')
pensize(10)
side=10
size=100
fillcolor('yellow')
begin_fill()
for i in range(side):
    fd(size)
    lt(360/side)
end_fill()
mainloop()    