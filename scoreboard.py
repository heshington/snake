from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.setposition(0,250)
        self.score = 0
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)




