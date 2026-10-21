"""BTSMRT"""

def main():
    """Main Function"""
    day, age, ht = input()[0], float(input()), float(input())
    check = (age < 14 and (ht < 90 or (ht <= 140 and day == "C"))) or (age >= 60 and day == "S")
    print("FREE" if check else "PAY")

main()
