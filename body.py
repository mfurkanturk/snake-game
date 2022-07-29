from turtle import Turtle

def drawBody(score):               #TODO: Her turda tekrar cizilecek body, skor miktari kadar 
    snake = []
    for i in range(score):         #* Skor miktarina gore uzunluk
        snake.append('')
        snake[i] = Turtle()
        snake[i].shape('circle')
        snake[i].penup()
    while True:
        xa = snake[0].xcor()
        ya = snake[0].ycor()
        snake[0].forward(20)
    
        for i in range(1,10):
            xb = snake[i].xcor()
            yb = snake[i].ycor()
            snake[i].goto(xa,ya)
            xa = xb
            ya = yb    
    
    


def bodyCol(location):                #TODO: Bir sonraki adimda yilanin basi body olan bir kareye geliyorsa end fonksiyonunu cagir   
    for i in range(len(location)):
        if location[0] == location[i]:
            endgame()                 #! Endgame function will be here
            
