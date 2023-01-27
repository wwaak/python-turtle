import time
target = 10


input(f"엔터를 누르고 {target}초를 셉니다.")
start = time.time()

input(f"{target}초 후에 다시 엔터를 누릅니다.")
end = time.time()
timedifferent = end - start
roundtime = round(timedifferent)

print(f"{end} - {start} 의 차이는 {roundtime}초입니다") 
print(f"{target}초를 맟췄겠지?")
if roundtime == target:
    print("축하합니다!")
else: 
    print("분발하세요")