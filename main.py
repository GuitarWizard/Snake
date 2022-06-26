import random
from turtle import Screen
import time
from snake import Snake
from food import Food
from snake_scoreboared import Scoreboard
from powerups import Powerup, Poison, Megapoison, Angryturtle

YLIMIT = 300
XLIMIT = 300

screen = Screen()
#print(screen.getshapes())

screen.setup(width=XLIMIT*2, height=YLIMIT*2)
screen.bgcolor("black")
screen.title("Snake Game - Turtle Train!")
screen.tracer(0)

game_is_on = True

snake = Snake()
food = Food()
score = Scoreboard()
poison_count = 1
powerup = Powerup()
poison = Poison()
mega_poison = Megapoison()
angry_turtle = Angryturtle()

# start_powerup_trigger = random.randint(0, 10)
# if start_powerup_trigger >= POWERUP_TRIGGER:
#     powerup= Powerup()
# else:
#     pass

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#score.display_score()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        score.scored()
        snake.grow()
        powerup.refresh()
        poison.refresh()
        print(score.score)
        angry_turtle.refresh()
        if score.score >= 100:
            mega_poison.refresh()

    if snake.head.distance(poison) < 15:
        poison_count += 1
        poison.refresh()
        powerup.refresh()
        score.penalty()
        # snake.grow()
        for _ in range (0,poison_count):
            snake.grow()

    if snake.head.distance(powerup) < 15:
        powerup.refresh()
        score.powerup_score()
        print(score.score)

    if snake.head.distance(mega_poison) < 15:
        poison.refresh()
        mega_poison.refresh()
        score.megapenalty()
        poison_count +=3
        for _ in range (0, poison_count):
            snake.grow()


    #detect collision with the wall
    if snake.head.xcor() > XLIMIT or snake.head.xcor() < -1*XLIMIT\
            or snake.head.ycor() > YLIMIT or snake.head.ycor() < -1*YLIMIT:
        game_is_on = False
        score.game_over()

    #detect body collision
    #if head collides with any segment in the tail:
        #game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on = False
            score.game_over()












screen.exitonclick()