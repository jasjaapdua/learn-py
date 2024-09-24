'''
    Snake is the main protagonist of the PySnake game.
'''

from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SPEED = 20

# Directions
DOWN = 270
LEFT = 180
UP = 90
RIGHT = 0

# Screen size
UPPER_BOUND = 300
LOWER_BOUND = -300


class Snake:
    '''
        Snake class represents a snake object which is made of a list of
        Turtle objects.
    '''
    def __init__(self):
        self.segments = []
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape='square')
            new_segment.color('green')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
        self.segments[0].color('yellow')

    def move_snake_forward(self):
        '''
            Moves the snake forward.
        '''
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_SPEED)

    def eat_food(self):
        '''
            Consumes food and makes the snake grow.
        '''
        new_segment = Turtle(shape='square')
        new_segment.color('green')
        new_segment.penup()
        self.segments.append(new_segment)

    def up(self):
        '''
            Makes the snake head north if it is not heading south.
        '''
        if self.segments[0].heading() != DOWN:
            self.segments[0].seth(UP)

    def down(self):
        '''
            Makes the snake head south if it is not heading north.
        '''
        if self.segments[0].heading() != UP:
            self.segments[0].seth(DOWN)

    def left(self):
        '''
            Makes the snake head lef if it is not heading right.
        '''
        if self.segments[0].heading() != RIGHT:
            self.segments[0].seth(LEFT)

    def right(self):
        '''
            Makes the snake head right if it is not heading left.
        '''
        if self.segments[0].heading() != LEFT:
            self.segments[0].seth(RIGHT)

    def wall_collide(self):
        '''
            If the snake runs into a wall, it reappears on the
            other side of the screen - maintain continuous gameplay.
        '''
        head = self.segments[0]
        head_x = self.segments[0].xcor()
        head_y = self.segments[0].ycor()
        if head.heading() == LEFT and head_x <= LOWER_BOUND:
            head.goto(UPPER_BOUND, head_y)
        elif head.heading() == RIGHT and head_x >= UPPER_BOUND:
            head.goto(LOWER_BOUND, head_y)
        elif head.heading() == DOWN and head_y <= LOWER_BOUND:
            head.goto(head_x, UPPER_BOUND)
        elif head.heading() == UP and head_y >= UPPER_BOUND:
            head.goto(head_x, LOWER_BOUND)
