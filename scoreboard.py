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
        with open("../../Desktop/data.txt") as file:
            self.high_score = int(file.read())
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if int(self.score) > int(self.high_score):

            with open("../../Desktop/data.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        with open("data.txt") as file:
            self.high_score = file.read()
        self.update_scoreboard()

