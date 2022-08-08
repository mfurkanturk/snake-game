from turtle import Screen, Turtle
from snake_body import SnakeBody
from food import Food
import time
my_screen = Screen()
my_screen.tracer(0) #tracer görüntü akşını keser 
my_screen.setup(width=600,height=600) 
my_screen.title("Snake Game")
my_screen.bgcolor("lightblue")
snake = SnakeBody()
snake.hideturtle() 
snake.create_snake() # 3 segmentli bir yılan yaratılır
my_screen.listen() #tuşları aktif hale getirir
my_screen.tracer(0) #tracer görüntü akşını keser
def up_fun():
    headings =snake.snake_segment[0].heading()
    if headings != 270.0 : #yılanın kendi içinden geçmesi engellenmiştir.
       snake.snake_segment[0].setheading(90)
def down_fun():
    headings =snake.snake_segment[0].heading()
    if headings != 90.0 :#yılanın kendi içinden geçmesi engellenmiştir.
        snake.snake_segment[0].setheading(270)
def east_fun():
    headings =snake.snake_segment[0].heading()
    if headings != 180.0 :#yılanın kendi içinden geçmesi engellenmiştir.
        snake.snake_segment[0].setheading(0)
def west_fun():
    headings =snake.snake_segment[0].heading()
    if headings != 0.0 and 360.0 :#yılanın kendi içinden geçmesi engellenmiştir.
        snake.snake_segment[0].setheading(180)
my_screen.update() #update olay örgüsü gerçekleştikten görüntü akışını günceller
my_screen.onkey(up_fun,"w")
my_screen.onkey(down_fun,"s")
my_screen.onkey(east_fun,"d")
my_screen.onkey(west_fun,"a")

food = Food() # yılanın yemi classtan çağrılır
food.fooding() # random bir alana yılan yemi gelir
my_screen.update()#update olay örgüsü gerçekleştikten görüntü akışını günceller
score = Turtle()  #score tablosu yaratılır
score.hideturtle()
score.penup()
score.goto(0,250)
control = True #While Döngüsünü kontrol eder
score_num = 0
while control ==  True :
    my_screen.tracer(0) #tracer görüntü akşını keser (döngü tamamlana kadar)
    snake.snake_move()
    if food.distance(snake.snake_segment[0]) < 18:
        snake.snake_food() #yılanın boyu uzatılır 
        food.clearfooding() #yılanın yemi silinir ve random konuma yeni bie yem bırakılır
        score_num = score_num+1 #skor tablosuna ekleme yapılır
        score.clear()
        score.write(f"Score: {score_num}", align="center", font=('Arial',20,'bold') )
    #Buraya if yapısı ile birlikte distance kullanmak yerine x ve y kordinatlra olan uzaklıklık hesabı yapılması gerekir
    #bkz. xcor ve ycor fonksiyonları 
    #yılanın ekranın duvarlarına çarptığı zaman oyunun bitmesi sağlanacak.
    #Buraya for döngüsü ve if yapısı ile distance fonksiyonu kullanılarak yılanın kendi segmentlerine çarptığı zaman oyunun bitmesi sağlanacak.
    # distance kullanırken for döngüsünde yılanın kendi segmentini çıkartmayı unutmakamk gerekir. segemnt[1]den başlaması lazım yoksa 
    #sürekli yılanın başı kendıne çarpacaktır.
    my_screen.update() #while döngüsünün sonunda ekran güncellenir
    time.sleep(0.1) 
#Görkem AVCI 
my_screen.exitonclick()


