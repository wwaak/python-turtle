import turtle as t
import random

bad_turtle = t.Turtle()
bad_turtle.shape("turtle")
bad_turtle.color("red")
bad_turtle.speed(0)
bad_turtle.up()
bad_turtle.goto(0, 200)

food = t.Turtle()
food.shape("circle")
food.color("green")
food.speed(0)
food.up()
food.goto(0, -200)

def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)


def play():
    t.forward(10)
    ang = bad_turtle.towards(t.pos())
    bad_turtle.setheading(ang)
    bad_turtle.forward(9)



    if t.distance(food) < 12:
        star_x = random.randint(-230, 230)
        star_y = random.randint(-230, 230)
        food.goto(star_x,star_y)
    if t.distance(bad_turtle) >= 12:
        t.ontimer(play, 100)

t.setup(500, 500)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()

t.color("white")

t.onkeypress(turn_right, "Right")

t.onkeypress(turn_up, "Up")

t.onkeypress(turn_left, "Left")

t.onkeypress(turn_down , "Down")
t.listen()
play()



t.mainloop()