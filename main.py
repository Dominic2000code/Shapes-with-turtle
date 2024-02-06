import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("green")
turtle.colormode(255)


# Dashed lines
# for _ in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# shapes
# def draw_shape(color, sides):
#     angle = 360 / sides
#     tim.pencolor(color)
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for n_sides in range(3, 11):
#     draw_shape(random_color(), n_sides)

# # Triangle
# draw_shape("gold", 3)
# # Square
# draw_shape("goldenrod", 4)
# # Pentagon
# draw_shape("goldenrod1", 5)
# # hexagon
# draw_shape("goldenrod2", 6)
# # heptagon
# draw_shape("goldenrod3", 7)
# # Octagon
# draw_shape("goldenrod4", 8)
# # Nonagon
# draw_shape("gold1", 9)
# # Decagon
# draw_shape("gold2", 10)

# Random walk
# tim.pensize(10)
# tim.speed("fastest")
# direction = [0, 90, 180, 270]
#
# for n in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(choice(direction))

# Drawing a spirograph
def draw_spirograph(gap_size):
    tim.speed("fastest")
    for n in range(0, 361, gap_size):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(n)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
