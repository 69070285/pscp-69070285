"""Increase Decrease"""

number1 = float(input())
number2 = float(input())
number3 = float(input())

if number1 < number2 < number3:
    print("increasing")
elif number1 > number2 > number3:
    print("decreasing")
else:
    print("neither")
