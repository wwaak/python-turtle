# num= input("숫자를 입력하세요")
# nameoji = int(num) % 2
# if nameoji == 0:
#     print(str(num)+"은(는) 2의 배수입니다..")
# else:
#     print(str(num)+"은(는) 2의 배수가 아닙니다.")


num = input("숫자를 입력하세요.")
divide = input("나눌 값을 선택하세요:")
nameoji = int(num) % int(divide)
if nameoji  == 0:
    print("나머지가 없습니다.")
else:
    print("나머지 값은:" + str(nameoji) + "입니다.")