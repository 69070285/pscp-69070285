"""[MINI EXAM] Sairahat"""

def main():
    """Main Function"""
    data = input()

    if data[:2] == "68" and data[2:4] == "07" and 1 <= int(data[4:]) <= 328:
        print("Yes")
    else:
        print("No")

main()
