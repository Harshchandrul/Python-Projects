from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north. If you get stuck, check the video walkthrough in Step 3.


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        
    def position_reset(self):
        self.goto(STARTING_POSITION)
        
    def go_up(self):
        self.forward(MOVE_DISTANCE)
        # new_y = self.xcor() + 10
        # self.goto(0, new_y)