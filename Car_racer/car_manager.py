from turtle import Turtle
import random 

COLORS = ['red', 'orange', 'blue', 'green', 'purple', 'pink', 'cyan']
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10

class CarManager:
    
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:                
            new_car = Turtle('square')
            # new_car.shape('square')
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            y_position = random.randint(-250, 250)
            new_car.goto(300 , y_position)
            self.all_cars.append(new_car)
        
    def increase_speed(self):
        self.speed += MOVE_INCREMENT
        
    def move_forward(self):
        for car in self.all_cars:
            car.backward(self.speed)

        