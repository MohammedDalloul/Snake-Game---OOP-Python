from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        self.score = 0
        super().__init__()
        with open("high_score_file.txt") as data:
            self.highest_score = int(data.read())
        self.shape("turtle")
        self.penup()
        self.goto(x=0, y=280)
        self.color("white")
        self.write(arg=f"Score : {self.score}", align=ALIGN, font=FONT, move=False)
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(arg=f"Score : {self.score}  Highest Score : {self.highest_score}", align=ALIGN, font=FONT, move=False)

    def restart_game(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("high_score_file.txt", mode="w") as data:
                data.write(f"{self.highest_score}")

        self.score = 0
        self.score_update()


    def increase_score(self):
        self.score += 1
        self.score_update()


