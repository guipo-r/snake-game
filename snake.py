# Imports
from turtle import Turtle


#  Constants
Y_POS = 0
X_POS = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# Definicion de la clase Snake
class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for n in range(3):
            new_square = Turtle('square')
            new_square.penup()
            new_square.color('green')
            new_square.setposition(x=X_POS[n], y=Y_POS)
            self.squares.append(new_square)

    def move(self):
        for item in range(len(self.squares) - 1, 0, -1):  # Hago que cada square vaya a la posicion del que le precede
            new_x = self.squares[item - 1].xcor()
            new_y = self.squares[item - 1].ycor()
            self.squares[item].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)  # Muevo el primer square hacia adelante

    def add_square(self):
        new_square = Turtle('square')
        new_square.penup()
        new_square.color('green')
        last_x = self.squares[-1].xcor() - 20
        last_y = self.squares[-1].ycor() - 20
        new_square.setposition(x=last_x, y=last_y)
        self.squares.append(new_square)

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
