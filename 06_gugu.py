num = input("몇단을 출력할까요?")
count = input("몇 개 출력할까요?")


for i in range(1,int(count) + 1):
    print(f"{num } * {i} = {int(num) * i}")