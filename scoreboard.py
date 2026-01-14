from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=250)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def scoring(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
