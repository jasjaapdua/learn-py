from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(5)

def move_backward():
    timmy.backward(5)

def turn_left():
    timmy.left(5)

def turn_right():
    timmy.right(5)

def clear_screen():
    timmy.reset()

screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear_screen)
screen.exitonclick()