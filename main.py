from turtle import Turtle, Screen
import body as mv

screen = Screen()

screen.listen()


screen.bgcolor("green")
screen.title("Snake game")
turk = Turtle()
mv.drawBody(5) #Örnek skor girdisi 5




screen.exitonclick()
