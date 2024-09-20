from turtle import Turtle, Screen
from math import pi
import random

def set_color(tim: Turtle):
    R = random.random()
    B = random.random()
    G = random.random()
    tim.color(R, G, B)

def draw_circle(tim: Turtle, angle_offset=0):
    set_color(tim)
    tim.left(angle_offset)
    tim.circle(100)

def spirograph(detail_level=50):
    tim = Turtle()
    tim.shape('turtle')
    tim.speed(10)
    angle_offset = (50/100) * 360
    angle_offset = 10
    for i in range(detail_level):
        draw_circle(tim, angle_offset)
    
    screen = Screen()
    screen.exitonclick()