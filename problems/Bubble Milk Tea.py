"""Bubble Milk Tea"""

def main():
    """Main Function"""

    data1 = input().split()
    data2 = input().split()
    pearl = data1[0]
    gram = float(data1[1])
    tea = data2[0]
    sweet = int(data2[1])
    amount = float(data2[2])
    mix = {
        "R" : {1 : 12, 2 : 18, 3 : 25},
        "T" : {1 : 15, 2 : 20, 3 : 30},
        "M" : {1 : 10, 2 : 15, 3 : 20}
    }
    mix = mix[tea][sweet]

    match pearl:
        case "H":
            result = (gram * 5) + (mix * amount)
        case "O":
            result = (gram * 3) + (mix * amount)
        case _:
            result = (gram * 2) + (mix * amount)

    if not result % 1:
        print(int(result))
    else:
        print(result)

main()
