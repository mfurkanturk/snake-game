from turtle import Turtle, Screen
from food import food
import random , time
screen = Screen()
screen.screensize(canvwidth=600, canvheight=600, bg="green")
screen.title("Snake game") 
snake = []
def drawBody(score):               #TODO: Her turda tekrar cizilecek body, skor miktari kadar 
    global snake
    dist = food()
    for i in range(score):         #* Skor miktarina gore uzunluk
        snake.append('')
        snake[i] = Turtle()
        snake[i].shape('square')
        snake[i].penup()
        snake[0].speed(2)
    while True:
        screen.tracer(0) #delay
        xa = snake[0].xcor()
        ya = snake[0].ycor()
        snake[0].forward(10)
        for i in range(1,score):
            xb = snake[i].xcor()
            yb = snake[i].ycor()
            snake[i].goto(xa,ya)
            xa = xb
            ya = yb    
        
        
        def up():
            if snake[0].heading() != 270: 
                snake[0].speed(0)
                snake[0].setheading(90)
                snake[0].speed(2)
                
        def down():
            if snake[0].heading() != 90: 
                snake[0].speed(0)
                snake[0].setheading(270) 
                snake[0].speed(2)
        def right():
            if snake[0].heading() != 180: 
                snake[0].speed(0)
                snake[0].setheading(0) 
                snake[0].speed(2)
        def left():
            if snake[0].heading() != 0: 
                snake[0].speed(0)
                snake[0].setheading(180) 
                snake[0].speed(2)
        if snake[0].distance(dist) < 20:
            print("Terminal Kontrol İstasyonu") #Buraya skor +1 ve yılan uzunluğu +1  kod yazılacak
            apsis = random.randint(-300,300)
            ordinat = random.randint(-300,300)
            dist.goto(apsis,ordinat)
            
        screen.listen()
        screen.onkey(up, "Up") 
        screen.onkey(down, "Down") 
        screen.onkey(right, "Right") 
        screen.onkey(left, "Left") 
        screen.update() #delay
        time.sleep(0.1) #delay
