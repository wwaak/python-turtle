import turtle as t
import time

t.bgcolor("black")
t.color("white")

t.begin_fill()


for k in range(0,4):
    print("k",k)
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

t.end_fill()


t.left(225)
t.forward(40)

angle=89
t.color("pink")
t.speed(0)

for x in range(800):
    t.forward(x)
    t.left(angle)








time.sleep(1000)