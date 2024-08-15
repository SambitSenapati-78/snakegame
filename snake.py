from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# creating a snake body

class Snake:
    def __init__(self):
        self.snake_tail = []
        self.create_snake()
        self.move()
        self.head = self.snake_tail[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.snake_body(position)

    def snake_body(self, position):
        scoot = Turtle()
        scoot.penup()
        scoot.shape("square")
        scoot.color("white")
        scoot.goto(position)
        self.snake_tail.append(scoot)

    def extend(self):
        self.snake_body(self.snake_tail[-1].position())
    def move(self):
        for num in range(len(self.snake_tail) - 1, 0, -1):
            new_x = self.snake_tail[num - 1].xcor()
            new_y = self.snake_tail[num - 1].ycor()
            self.snake_tail[num].goto(new_x, new_y)
        self.snake_tail[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
