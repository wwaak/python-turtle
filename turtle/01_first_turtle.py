#라이브러리
import turtle as t
import time

DELAY = 0.5
t.shape("turtle")

for k in range(0,10):
    print("k:", k)
    #거북이 한바퀴 돌리기
    for i in range(0, 4):
        print("i:", i)
        t.forward(50)
        time.sleep(DELAY)
        t.right(90)
        time.sleep(DELAY)

    t.forward(25)
    
        
        
        

time.sleep(1000)