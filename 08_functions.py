#3배 자판기 생성 (def 를 함수라고 한다.)
def multiply3(money):
    print(f"자판기에 들어온 금액은 {money}")
    return money * 3

#최초 돈
num = 500

#multipl3 자판기에 num을 투입
result = multiply3(num)

print(f"결과는 {result} 입니다.")

num2 = 10000
result2 = multiply3(num2)
print(f"결과는 {result} 입니다.")