from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.x_score = 0
        self.y_score = 0
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(-100, 250)
        self.write("Player 1", align="center", font=("Courier", 20, "normal"))
        self.goto(-100, 220)
        self.write(self.x_score, align="center", font=("Courier", 20, "normal"))
        self.goto(100, 250)
        self.write("Player 2", align="center", font=("Courier", 20, "normal"))
        self.goto(100, 220)
        self.write(self.y_score, align="center", font=("Courier", 20, "normal"))

    def x_point(self):
        self.x_score += 1
        self.update_score()

    def y_point(self):
        self.y_score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 36, "normal"))
