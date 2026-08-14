"""[LEARNING LOGS] Lottery"""

def main():
    """Main Function"""
    data = input().split()
    correct = data[0] + data[1]
    data = input().split()
    buy = data[0] + data[1]

    if buy == correct:
        print("1000000")
    elif buy[0] != correct[0] and buy[1:] == correct[1:]:
        print("100000")
    elif buy[3:] == correct[3:]:
        if buy[0] == correct[0]:
            print("2000")
        else:
            print("200")
    elif buy[4:] == correct[4:]:
        if buy[0] == correct[0]:
            print("1000")
        else:
            print("100")
    elif buy[0] == correct[0]:
        print("20")
    else:
        print("0")

main()
