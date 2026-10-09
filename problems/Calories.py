"""Calories"""

def main():
    """Main Function"""
    total = 0
    cal = [100, 120, 200, 60]

    while True:
        cmd = int(input())
        if cmd == 5:
            print("Bye Bye")
            print("Total Calories:", total)
            break
        total += cal[cmd - 1]

main()
