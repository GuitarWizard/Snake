from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 13, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.scoreboard = Turtle()
        self.scoreboard.penup()
        self.hideturtle()
        self.scoreboard.color("white")
        self.scoreboard.goto(x=0, y=275)
        self.scoreboard.hideturtle()
        self.scoreboard.write(f"SCORE: {self.score}", False, align=ALIGNMENT, font=FONT)
        self.score_multiplier = self.score *0.5


    def scored(self):
        self.scoreboard.clear()
        self.score += 1
        self.scoreboard.write(f"SCORE: {self.score}", False, align=ALIGNMENT, font=FONT)


    def powerup_score(self):
        self.scoreboard.clear()
        self.score_bonus = int(self.score * 0.25)
        self.score += 3
        self.score += self.score_bonus
        self.scoreboard.write(f"SCORE: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def penalty(self):
        self.scoreboard.clear()
        self.score -= 3
        self.scoreboard.write(f"SCORE: {self.score}", False, align=ALIGNMENT, font=FONT)

    def megapenalty(self):
        self.scoreboard.clear()
        self.score_megapenalty = int(self.score * 0.40)
        self.score -= self.score_megapenalty
        self.scoreboard.write(f"SCORE: {self.score}", False, align=ALIGNMENT, font=FONT)
