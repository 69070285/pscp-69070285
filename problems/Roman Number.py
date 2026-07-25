"""Roman Number"""

number = int(input())

if number < 0:
    print("Error : Please input positive number")
elif not number or number > 9:
    print("Error : Out of range")
elif number <= 3:
    print("I" * number)
elif number == 4:
    print("IV")
elif number <= 8:
    print("V", "I" * (number % 5), sep="")
else:
    print("IX")
