from turtle import Turtle
class SnakeBody(Turtle): #class yapısı kodların birbirleriyle iletişimini kolaylaştıracaktır
    def __init__(self) :#nesne yaratılması ile birlikte gelen oto durumlar
        super().__init__()#turtle nesnesinden inherit edilerek turtle fonskiyonlarının kullanılması sağlanmıştır
        self.penup()
        self.shape("square")
        self.snake_segment = []
        
    def create_snake(self):
        x_cor = 0
        for _ in range(3):
            my_snake = SnakeBody()
            my_snake.fillcolor("Black")
            my_snake.goto(x_cor,0)
            self.snake_segment.append(my_snake)
            
    
    def snake_move(self):
            head_position = self.snake_segment[0].position()
            self.snake_segment[0].forward(20)
            for _ in range(len(self.snake_segment)-1):
                n_head_pos = self.snake_segment[_ + 1].position()
                self.snake_segment[_ + 1].goto(head_position)
                head_position = n_head_pos
            
    def snake_food(self):
        my_snake = SnakeBody()
        my_snake.goto(self.snake_segment[-1].position())
        my_snake.fillcolor("Black")
        self.snake_segment.append(my_snake)
      