import turtle as t

#오른쪽으로 90도 회전하는 함수
def turn_right():
    t.right(90)

t.shape('turtle')

#특정 시간마다 작업을 수행
t.ontimer(turn_right, 1000)

t.mainloop()