from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEP_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snakes_st = []
        self.create_snakes()

    def create_snakes(self):
        for position in START_POSITIONS:
            self.add_slice(position)


    def add_slice(self, position):
        snake = Turtle()
        snake.color("green")
        snake.shape("square")
        snake.penup()
        snake.goto(position)
        self.snakes_st.append(snake)

    def extend_snake(self):
        self.add_slice(self.snakes_st[-1].position())

    def move(self):
        for num in range(len(self.snakes_st) - 1, 0, -1):
            newx = self.snakes_st[num - 1].xcor()
            newy = self.snakes_st[num - 1].ycor()
            self.snakes_st[num].goto(newx, newy)
        self.snakes_st[0].fd(STEP_DISTANCE)


    def up(self):
        if self.snakes_st[0].heading() != 270:
            self.snakes_st[0].setheading(90)

    def down(self):
        if self.snakes_st[0].heading() != 90:
            self.snakes_st[0].setheading(270)

    def turn_rt(self):
        if self.snakes_st[0].heading() != 180:
            self.snakes_st[0].setheading(0)

    def turn_lt(self):
        if self.snakes_st[0].heading() != 0:
            self.snakes_st[0].setheading(180)


    def reset_snake(self):
        for seg in self.snakes_st:
            seg.goto(1000, 1000)
        self.snakes_st.clear()
        self.create_snakes()




