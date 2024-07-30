from turtle import Turtle
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.shape('turtle')
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(-240, 250)
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def update(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def game_over(self):
        #self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=FONT)
