"""[MIDTERM] FakeThaiPlus"""

def main():
    """Main Function"""
    name = input()
    age = int(input())
    money = int(input())
    member = input()
    family = int(input())
    role = ""

    if age >= 18 and (member == "Y" or 0 <= money <= 30000):
        if member == "Y" or money <= 15000:
            role = "GOLD"
            money = 3000
        else:
            role = "SILVER"
            money = 1500

        if family >= 3:
            money += 500

        print(f"{name} {role} {money}")
    else:
        print(f"{name} NOT ELIGIBLE")

main()
