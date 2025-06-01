from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('JetBrains Mono', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.update_level()
        
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over" , align=ALIGNMENT, font=FONT)
        

    def update_level(self):
        self.clear()
        self.penup()
        self.goto(-230, 255)
        self.hideturtle()
        self.write(f'Level: {self.level}', align=ALIGNMENT, font=FONT)
        
    def level_up(self):
        self.level += 1
        self.update_level()