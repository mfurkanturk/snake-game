from turtle import Turtle
from random import randint


class Food(Turtle):  # class yapısı kodların birbirleriyle iletişimini kolaylaştıracaktır

    def __init__(self) :  # nesne yaratılması ile birlikte gelen oto durumlar
        super().__init__()  # turtle nesnesinden inherit edilerek turtle fonskiyonlarının kullanılması sağlanmıştır
        self.shape("circle")
        self.shapesize(1)
        self.penup()   
        self.color("Black")

    def fooding(self):
        x = randint(-270,270)
        y = randint(-270,240)
        self.goto(x,y)

    def clearfooding(self):
        self.clear()
        x = randint(-270,270)
        y = randint(-270,240)
        self.goto(x,y)
       
