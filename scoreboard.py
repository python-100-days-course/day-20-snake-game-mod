from turtle import Turtle

ALIGNMENT = "left"
ALIGNMENT_2 = "center"
FONT = ('Courier', 14, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.goto(x=-30, y=270)
        self.color("white")
        self.score = 0
        with open("data.txt") as data: # Day 25 - Oct-14-2024
            self.high_score = int(data.read()) # Day 25 - Oct-14-2024
        self.hideturtle()
        self.display()

    def display(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    # Day 25 - Oct-14-2024 - high score mod
    def reset_snake(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data: # Day 25 - Oct-14-2024
                data.write(str(self.high_score)) # Day 25 - Oct-14-2024, save the new high score to txt file
        self.score = 0
        self.display()

    # Day 25 - Oct-14-2024 - commented out, use reset() instead
    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write("GAME OVER", False, align=ALIGNMENT_2, font=FONT)

    def increase(self):
        self.score += 1
        self.display()