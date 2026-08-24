"""[MIDTERM] Units"""

def main():
    """Main Function"""
    number = float(input())
    unit1 = input()
    unit2 = input()

    if unit1 == unit2:
        print(f"{number:.4f}")
    else:
        if unit1 == "NIU":
            number *= 1920
        elif unit1 == "KUEP":
            number *= 160
        elif unit1 == "SOK":
            number *= 80
        elif unit1 == "WA":
            number *= 20

        if unit2 == "NIU":
            print(f"{number / 1920:.4f}")
        elif unit2 == "KUEP":
            print(f"{number / 160:.4f}")
        elif unit2 == "SOK":
            print(f"{number / 80:.4f}")
        elif unit2 == "WA":
            print(f"{number / 20:.4f}")
        else:
            print(f"{number:.4f}")

main()
