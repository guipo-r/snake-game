from turtle import Turtle

# Constants
ALIGNMENT = "center"
FONT = ('Courier', 12, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor('white')
        self.hideturtle()

    def game_over(self):
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
