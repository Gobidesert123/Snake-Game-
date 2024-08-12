from turtle import Turtle
# INCREMENTING BY 20, also note that creating constants are named with capitals
POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE_MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.diff_snakes = []
        self.create_snake() # Notice how you can create methods and call them here
        self.leader = self.diff_snakes[0] # This is the first block (snake_head)

    # Creating snake
    def create_snake(self):
        for position in POSITION:
           self.add_segment(position)

    # This will help position the snake
    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.diff_snakes.append(snake)

    # This will add a new snake, and give it the position of the last snake.
    def extend(self):
        self.add_segment(self.diff_snakes[-1].pos())

    '''
    def add_snake(self):
        # adds a new snake to the bigger snake
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        self.diff_snakes.append(snake)
    '''
    def move(self):
        # Note that you have to take account of the bottom and left walls as-well
        # and the value 280 has to change.
        '''
        testing different code
        if self.diff_snakes[0].xcor() >= 300 or self.diff_snakes[0].ycor() >= 300:
            game_continue = False
            return game_continue
        '''
        # We are iterating through the diff_snakes backwards and then as the snake moves
        # we decrement and loop through all snakes.
        for seg_num in range(len(self.diff_snakes) - 1, 0, -1):
            new_x = self.diff_snakes[seg_num - 1].xcor()
            new_y = self.diff_snakes[seg_num - 1].ycor()
            self.diff_snakes[seg_num].goto(new_x, new_y)
        self.leader.forward(DISTANCE_MOVE) # This is so it continuously moves forward

    # Resetting the snake to original location and size.
    def reset_snake(self):
        for snake in self.diff_snakes:
            snake.goto(1000,1000) # This is so the old snake is off the screen
        self.diff_snakes.clear()  # This clears the list and now is empty
        self.create_snake()
        self.leader = self.diff_snakes[0]

    # Creating different movements.
    def up(self):
        if self.leader.heading() != DOWN:
            self.leader.setheading(UP)

    def down(self):
        if self.leader.heading() != UP:
            self.leader.setheading(DOWN)

    def left(self):
        if self.leader.heading() != RIGHT:
            self.leader.setheading(LEFT)

    def right(self):
        if self.leader.heading() != LEFT:
            self.leader.setheading(RIGHT)

