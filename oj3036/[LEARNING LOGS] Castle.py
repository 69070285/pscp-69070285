"""[LEARNING LOGS] Castle"""

num = int(input())
floor = 1
max_num = 1
stack_num = 3
smash = 0

while max_num < num:
    smash += 2
    floor += 1
    max_num += stack_num
    stack_num += 2

if floor % 2 and num % 2:
    print(smash)
elif not floor % 2 and not num % 2:
    print(smash)
else:
    print(smash - 1)
