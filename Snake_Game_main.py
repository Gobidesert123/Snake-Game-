# Importing all files/classes/modules
from turtle import Screen
from snake import Snake
from food_snake import Food
from scoreboard_snake import Scoreboard
import time

# ******************************* Setting up the screen ********************************
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game- Gobind Kailey")

'''
When the line of code below is turned off (0) we are able to turn off the animation and then 
later use update to refresh the screen. 
'''
screen.tracer(0)

# Creating Objects
snake = Snake()
food = Food()
score = Scoreboard()

# functions do not need to be called in inputs, so do not include ()
'''
# This will allow the screen to listen to our clicks and run functions as it notices
# a familiar one get pressed.
'''
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_continue = True
while game_continue:
    # Updating the screen
    screen.update()
    # Adding a small delay so that the game runs more smoothly
    time.sleep(0.1)
    snake.move()
    # Detect collision of snake with food.
    # Note that this checks the distance from the center of food to snake
    if snake.leader.distance(food) < 20:
        food.refresh() # Places the food in a new random location.
        score.score_up() # This increases the score displayed.
        snake.extend() # This extends the length of the snake.

    # Detect collision with wall.
    if snake.leader.xcor() > 280 or snake.leader.xcor() < -290 or snake.leader.ycor() > 290 or snake.leader.ycor() < -290:
        score.reset_score()
        snake.reset_snake()

    # Detect collision with Tail.
    '''
    The reason we start at 1 and not 0 is because when we are looping through the 
    snake and the first snake is the head snake and it will always be true that the head snake 
    is in contact <10. 
    This is one way of doing it. 
    for i in range(1, len(snake.diff_snakes)):
        if snake.leader.distance(snake.diff_snakes[i]) < 10:
            game_continue = False
            score.game_over()
            
    In the example below we are we are using string slicing. 
    '''
    for location in snake.diff_snakes[1:]:
        if snake.leader.distance(location) < 10:
            score.reset_score()
            snake.reset_snake()
screen.exitonclick()

