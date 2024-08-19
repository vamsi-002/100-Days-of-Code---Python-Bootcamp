from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=-10, y=270)
        self.write(f"Score= {self.score}", False, align="center", font=("Arial", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score= {self.score}", False, align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align="center", font=("Arial", 15, "normal"))