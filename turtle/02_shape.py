
import turtle as t
import time

DELAY = 0.1
t.shape("turtle")
for k in range(0,9):
    print("k:",k)
    t.forward(100)
    t.left(120)

for i in range(0,8):
    print("i",i)
    t.forward(100)
    t.left(90)

t.circle(50)

time.sleep(1000)