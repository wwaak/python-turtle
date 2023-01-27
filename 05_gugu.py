num = input("몇단을 출력할까요?")
numbers = [1,2,3,4,5,6,7,8,9]

num_int = int(num)
print("num is...",num)
for i in numbers:
    print(str(num) + " * "+ str(i) + " = " + str(num_int * i))