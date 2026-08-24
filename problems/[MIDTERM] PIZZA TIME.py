"""[MIDTERM] PIZZA TIME"""

from math import ceil

def main():
    """Main Function"""
    people = int(input())
    perperson = int(input())
    cutout = int(input())
    need = people * perperson
    amount = ceil(need / cutout)

    print(need)
    print(amount)
    print(amount * cutout - need)

main()
