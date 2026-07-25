"""Seven"""

number = int(input())
check = (number % 4000000) % 4

match check:
    case 1:
        print("7")
    case 2:
        print("9")
    case 3:
        print("3")
    case _:
        print("1")
