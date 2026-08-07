"""Multiplication Table"""

def main():
    """Main Function"""
    number = int(input())

    for i in range(1, 13):
        print(f"{number} * {i} = {number * i}")

main()
