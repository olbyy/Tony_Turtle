from turtle import Turtle, Screen, colormode
import random
import colorgram


def draw_circle(t, c):
    t.pendown()
    t.pencolor("white")
    t.fillcolor(c)
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()


def gen_color(c):
    random_number = random.randint(0, len(c)-1)
    rand_color = c[random_number]
    r = rand_color.rgb.r
    g = rand_color.rgb.g
    b = rand_color.rgb.b
    tup = (r, g, b)
    return tup


def draw_dots(t, c):
    global x
    global y
    col = gen_color(c)
    draw_circle(t, col)

    if x > 240 and x != 0:
        x = 0
        y += 30
    else:
        x += 30

    t.goto(x, y)

tony = Turtle()
tony.pensize(1)
colormode(255)
tony.resizemode("auto")
tony.speed("fastest")

colors = colorgram.extract('download.png', 10)

x = 0
y = 0

while y < 300:
    draw_dots(tony, colors)

my_screen = Screen()
my_screen.exitonclick()

