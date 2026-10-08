"""[ MINI EXAM ] Item checker"""

def main():
    """Main Function"""
    data = input().lower().split()
    target = input()

    if target.lower() in data:
        print(f"{target} is in the list")
    else:
        print(f"{target} is not in the list")

main()
