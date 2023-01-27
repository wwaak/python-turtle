def losemoney(money):
    print(f"자판기에 들어온 금액은 {money}입니다.")
    return money - 5000
num = 10000
result = losemoney(num)

print(f"결과는 {result}입니다.")