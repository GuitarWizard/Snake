# Snake? Snake? SNAAAAAAAAAAKE!!!!
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):

        for position in STARTING_POSITIONS:
            self.add_segment(position)

        #self.head= self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape("square")
        if position == (0, 0):
            new_segment.color("green")
            new_segment.goto(position)
            self.segments.append(new_segment)
        else:
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def grow(self):
        """not functioning properly yet. Adds a new segment to the snake"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # the range function in python is based
            # on the C language and does not
            # take keyword argument but they stand for this: (start = , end = , step = )
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):

        if self.head.heading() == 0 or self.segments[0].heading() == 180:
            self.head.setheading(90)
        else:
            pass

    def down(self):
        pass
        if self.head.heading() == 0 or self.segments[0].heading() == 180:
            self.head.setheading(270)
        else:
            pass

    def left(self):
        pass
        if self.head.heading() == 90 or self.segments[0].heading() == 270:
            self.head.setheading(180)
        else:
            pass

    def right(self):
        pass
        if self.head.heading() == 90 or self.segments[0].heading() == 270:
            self.head.setheading(0)
        else:
            pass


