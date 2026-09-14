"""Tuple's Sad life"""

def main():
    """Main Function"""
    text = tuple(input().split())
    target = input()
    search = text.index(target)
    count = text.count(target)

    for _ in range(count):
        print(*(str(search) * (count)))

main()
