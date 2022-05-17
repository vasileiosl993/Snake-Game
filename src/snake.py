from turtle import Turtle


class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            self.add_snake(i)

    def add_snake(self, position):
        start = 0
        x = Turtle()
        x.shape("square")
        x.color("white")
        x.penup()
        x.goto(x=start, y=0)
        start += 20
        self.snakes.append(x)

    def extend_snake(self):
        self.add_snake(self.snakes[-1].position())

    def move_snake(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[i - 1].xcor()
            new_y = self.snakes[i - 1].ycor()
            self.snakes[i].goto(new_x, new_y)

        self.snakes[0].forward(20)

    def up(self):
        if self.snakes[0].heading() != 270:
            self.snakes[0].setheading(90)

    def down(self):
        if self.snakes[0].heading() != 90:
            self.snakes[0].setheading(270)

    def right(self):
        if self.snakes[0].heading() != 180:
            self.snakes[0].setheading(0)

    def left(self):
        if self.snakes[0].heading() != 0:
            self.snakes[0].setheading(180)


