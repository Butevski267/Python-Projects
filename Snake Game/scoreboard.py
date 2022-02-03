from turtle import Turtle
FONT = ("Courier", 22, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="Center", font = FONT)
        self.hideturtle()
        
    
    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}", align="Center", font = FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align = "Center", font = FONT)
        self.hideturtle()