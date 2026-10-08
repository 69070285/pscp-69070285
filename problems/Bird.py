"""Bird"""

def main():
    """Main Function"""
    amount = int(input())
    tree = list(map(int, ("0 " + input() + " 0").split()))
    result = sum(1 for i in range(1, amount + 1) if tree[i - 1] < tree[i] > tree[i + 1])
    print(result)

main()
