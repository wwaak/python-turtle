import time

#1670134900.6746619 1670134900.6746619
input("엔터를 누르고 20초를 셉니다.")
start = time.time()


input("20초 후에 다시 엔터를 누릅니다.")
#1670134900.6746619 1670134900.6746619
end = time.time()



print(f"{end} - {start} 의 차이는 {round(end - start)}초입니다") 
print("20를 다 세었니?,못 맟췄으면 노력을 더 해봐!^^")
