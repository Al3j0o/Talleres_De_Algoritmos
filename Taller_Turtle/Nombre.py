
import turtle
import random

turtle.title("Nombre")
turtle.bgcolor("black")
turtle.screensize(300,300)

turtle.speed(0)
x=1
turtle.setposition(-300,300)
while(x<500):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    turtle.colormode(255)
    turtle.pencolor(r,g,b)

    turtle.forward(5+x)
    turtle.right(91)
    x+=1
y=1
turtle.penup()
turtle.goto(300,-300)
turtle.pendown()
while(y<500):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    turtle.colormode(255)
    turtle.pencolor(r,g,b)

    turtle.forward(5+y)
    turtle.right(91)
    y+=1

turtle.penup()
turtle.goto(0,0)
turtle.pencolor("white")

turtle.write("Alejandro",False,align="center",font=("Times new roman",100,"normal"))
turtle.mainloop()