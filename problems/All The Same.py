"""All The Same"""

number1 = float(input())
number2 = float(input())
number3 = float(input())

if number1 == number2 == number3:
    print("all the same")
elif number1 == number2 or number1 == number3 or number2 == number3:
    print("neither")
else:
    print("all different")
