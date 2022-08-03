from turtle import *
pensize(3)
pencolor('blue')
fillcolor('red')
for i in range(10,0,-1):
     begin_fill()
     circle(i*10)
     lt(25)
     end_fill()

mainloop()