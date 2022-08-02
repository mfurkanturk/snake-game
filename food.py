from turtle import Screen, Turtle
import random 
def food():
    #screen =Screen()
    #screen.screensize(canvwidth=600, canvheight=600, bg="green")
    turtle = Turtle()
    turtle.shape("circle")
    turtle.penup()
    turtle.shapesize(stretch_len=0.8,stretch_wid=0.8)
    turtle.color("black")
    apsis = random.randint(-300,300)
    ordinat = random.randint(-300,300)
    turtle.goto(apsis,ordinat)
    return turtle
    
