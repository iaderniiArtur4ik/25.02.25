import math
number=int(input("введите число:"))
print(math.factorial(number))



# ну или


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("введите число:"))
result = factorial(n)
print(result)