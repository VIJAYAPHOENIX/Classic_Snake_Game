from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.score_card()

    def score_card(self):
        self.write(f"score : {self.score}",align="center",font=("Arial",24,"normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("game over!", align="center", font=("Arial", 34, "normal"))


    def increment(self):
        self.score += 1
        self.clear()
        self.score_card()