import random
from turtle import Turtle
import time

POISON_TRIGGER = 5
POWERUP_TRIGGER = 8
ANGRY_TURTLE_TRIGGER = 5


class Powerup(Turtle):

    def __init__(self):
        super().__init__()

    def refresh(self):
        self.powerup_trigger = random.randint(0, 10)
        print(self.powerup_trigger)
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        if self.powerup_trigger >= POWERUP_TRIGGER:
            self.showturtle()
            self.goto(random.randint(-270, 270), random.randint(-270, 270))

        else:
            self.hideturtle()



class Poison(Turtle):
    def __init__(self):
        super().__init__()
        # self.shape("triangle")
        # self.penup()
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # self.color("red")
        # self.speed("fastest")
        # self.refresh()

    def refresh(self):
        self.poison_trigger = random.randint(0, 10)
        self.shape("circle")
        self.shapesize(14)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        if self.poison_trigger >= POISON_TRIGGER:
            self.showturtle()
            self.goto(random.randint(-270, 270), random.randint(-270, 270))
        else:
            self.hideturtle()
        self.goto(random.randint(-270, 270), random.randint(-270, 270))

class Megapoison(Turtle):
    """Really hurts - dont eat this"""
    def __init__(self):
        super().__init__()

    def refresh(self):
        self.poison_trigger = random.randint(0, 10)
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        if self.poison_trigger >= POISON_TRIGGER:
            self.showturtle()
            self.goto(random.randint(-270, 270), random.randint(-270, 270))
        else:
            self.hideturtle()

class Angryturtle(Turtle):
    """Snake Eating Turtle that walks across the field. Probably has to go into the snake
    move funciton in the other module - this crashes the program right now."""
    def __init__(self):
        super().__init__()

    def refresh(self):
        self.angry_trigger = random.randint(0, 10)
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        if self.angry_trigger >= ANGRY_TURTLE_TRIGGER:
            self.showturtle()
            self.goto( 0, random.randint(-270, 270))
            self.setheading(0)
            # while self.xcor()< 270:
            #     self.color("yellow")
            #     self.forward(10)
            #     time.sleep(0.5)
            #     self.color("red")
            #     time.sleep(0.5)

        else:
            self.hideturtle()