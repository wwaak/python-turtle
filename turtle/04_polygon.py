import turtle as t
import time

n = input("몇 각형을 그리시겠습니까? :")
n = int(n)

t.color("pink")

t.begin_fill()
for x in range(n):
    t.forward(50)
    t.left(360/n)


t.end_fill()

time.sleep(1000)
