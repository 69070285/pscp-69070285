"""Christmas Light"""

def main():
    """Main Function"""
    data = input().split()
    color = data[0]
    amount = int(data[1])
    count = 1
    result = []

    if color == "R":
        for _ in range(amount):
            match count:
                case 1:
                    result.append("Red")
                case 2:
                    result.append("Green")
                case _:
                    result.append("Blue")
                    count = 0
            count += 1
    elif color == "G":
        for _ in range(amount):
            match count:
                case 1:
                    result.append("Green")
                case 2:
                    result.append("Blue")
                case _:
                    result.append("Red")
                    count = 0
            count += 1
    else:
        for _ in range(amount):
            match count:
                case 1:
                    result.append("Blue")
                case 2:
                    result.append("Red")
                case _:
                    result.append("Green")
                    count = 0
            count += 1

    print(" ".join(result))

main()
