"""Christmas Light"""

def main():
    """Main Function"""
    data = input().split()
    color = data[0]
    amount = int(data[1])
    result = []

    match color:
        case "R":
            count = 1
        case "G":
            count = 2
        case _:
            count = 3

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

    print(" ".join(result))

main()
