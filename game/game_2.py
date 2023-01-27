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
def start():
    global playing
    if playing == False:
        playing = True.clear()
        play()

def play():
    global score
    global playing
    t.forward(10)
    if random.randint(1, 5) == 3:
        ang = bad_turtle.towards(t.pos())
        bad_turtle.setheading(ang)
    speed = score + 5

    if speed > 15:
        speed = 15
    bad_turtle.forward(speed)
    if t.distance(food)  < 12:
        text = " Score : " + str(score)
        message =  ("Game Over", text)
        playing = False
        score = 0
    if t.distance(food) <12:
        score = score + 1
        t.write(score)
        star_x = random.randint(-230, 230)
        star_y = random.randint(-230, 230)
        food.goto(star_x, star_y)
    if playing:
        t.ontimer(play, 100)

def message(m1, m2):
    t.clear()
    t.goto(0.-100)
    t.write(m1, False, "center", ("", 20))


        
