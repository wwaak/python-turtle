num = 3
dan = 1
#이렇게 하면 불편하다.
print(str(num) + " * " + str(num * dan))
#이렇게 해야 편하다/
print(f"{num} * {dan} = {num * dan}")