"""24D_Best_Before"""

def main():
    """Main Function"""
    data = [input() for _ in range(int(input()))]

    if any(int(d[:2]) > 12 for d in data) and all(int(d[2:4]) <= 12 for d in data):
        print("ddmmyy")
    elif any(int(d[2:4]) > 12 for d in data) and all(int(d[:2]) <= 12 for d in data):
        print("mmddyy")
    else:
        print("no clue")

main()
