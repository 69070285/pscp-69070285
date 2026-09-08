"""Pig"""

def main():
    """Main Function"""
    amount = int(input())
    pair = list(map(int, input().split()))
    result = []

    if amount == 1:
        print(max(pair[0], pair[1]))
    else:
        for i in range(0, amount * 2, 2):
            result.append(str(max(pair[i], pair[i+1])))

        print(" + ".join(result), "=", sum(list(map(int, result))))

main()
