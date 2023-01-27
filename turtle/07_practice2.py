import turtle as t
import time

def draw_one_wing():
    t.forward(80)
    t.left(90)
    t.forward(140)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(210)
    t.right(90)
    t.forward(140)
    t.left(90)

t.bgcolor("black")
t.color("white")

t.begin_fill()


for k in range(0,4):
    draw_one_wing()

t.end_fill()

t.speed(0)

t.left(225)
t.forward(40)

#삼각형을 그리는 코드

for x in range(500):
    if x % 3 == 0:
        t.color("blue")
    if x % 3 == 1:
        t.color("yellow")
    if x % 3 == 2:
        t.color("red")
    t.forward( x * 2)
    t.left(119)








time.sleep(1000)