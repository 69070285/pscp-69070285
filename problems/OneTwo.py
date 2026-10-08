"""OneTwo"""

def main():
    """Main Function"""
    amount = int(input())
    s1, s2 = "1", "2"

    if amount < 3:
        print(amount)
    else:
        for _ in range(amount - 2):
            result = s2 + s1
            s1 = s2
            s2 = result
        print(result)

main()
