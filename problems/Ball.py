"""Ball"""

def main():
    """Main Function"""
    bounce = float(input())
    count = 0

    while bounce >= 0.01:
        bounce *= 3/5
        count += 1

    print(count - 1)

main()
