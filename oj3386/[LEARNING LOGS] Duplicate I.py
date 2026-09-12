"""[LEARNING LOGS] Duplicate I"""

def main():
    """Main Function"""
    amount1 = int(input())
    amount2 = int(input())
    group1 = {input() for _ in range(amount1)}
    group2 = {input() for _ in range(amount2)}
    result = sorted(list(group1 & group2))

    if not result:
        print("Nope")
    else:
        for i in result[::-1]:
            print(i)

main()
