"""Swap Number"""

number = input()
first_number = int(number)
second_number = int(number[::-1])
operator = input()

if operator == "+":
    result = first_number + second_number
else:
    result = first_number * second_number

print(f"{first_number} {operator} {second_number} = {result}")
