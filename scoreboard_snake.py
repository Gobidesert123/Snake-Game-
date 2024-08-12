from turtle import Turtle

'''
Inherit the Turtle class
The scoreboard is supposed to be a turtle, which keeps track of the score 
'''
# This is just incase we want to change the alignment or the font,
# we would not have to go searching for the code.
ALIGNMENT = 'center'
FONT = ("Arial", 15, "normal")

# if snake_highscore isn't a file created this will auto create it for you.
with open("snake_highscore", mode='r') as reading_hs:
    current_hs = int(reading_hs.read())

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = current_hs
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_score()

    # This will showcase the score/ update it.
    def update_score(self):
        self.write(arg= f"Score: {self.score} High Score: {self.highscore}  ",
                   align= ALIGNMENT, font= FONT)


    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            # if the current score is greater than the hs, it will make that into the new hs.
            with open("snake_highscore", mode='w') as h_s:
                h_s.write(str(self.highscore))
        self.score = 0
        self.clear()
        self.update_score()
    def score_up(self):
        self.score += 1
        self.clear()
        self.update_score()


    def high_score(self):
        self.write(arg=" GAME OVER!  ", align=ALIGNMENT, font=FONT)


