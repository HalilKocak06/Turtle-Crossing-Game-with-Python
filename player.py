from turtle import Turtle

STARTING_POSITION = (0,-250)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto(0,-250)
        
    
    def move(self):
        self.forward(MOVE_DISTANCE)



    def reset_position(self):
        self.goto(0,-250)    