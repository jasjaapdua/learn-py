'''
    The main driver code for PySnake.
    Exports:
        
'''

import time
import random
from turtle import Screen
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('PySnake')
screen.tracer(0)

GAME_IS_ON = True

def pause():
    '''
        Pauses the game by changing the global game state
    '''
    global GAME_IS_ON
    GAME_IS_ON = not GAME_IS_ON
    if GAME_IS_ON:
        start()

def start():
    '''
        Starts the game, keeps playing while GAME_IS_ON is set to True
    '''
    while GAME_IS_ON:
        snake.move_snake_forward()
        screen.update()
        time.sleep(0.1)
        if snake.segments[0].distance(food) < 15:
            random_x = random.randint(-280, 280)
            random_y = random.randint(-280, 280)
            food.goto(random_x, random_y)
            snake.eat_food()
        snake.wall_collide()


snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(pause, 'space')

screen.exitonclick()
