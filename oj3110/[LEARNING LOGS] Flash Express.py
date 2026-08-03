"""[LEARNING LOGS] Flash Express"""

def main():
    """Main Function"""
    route = input()
    weight = float(input())

    match route:
        case "BKK CNX":
            print(f"{(weight * 30) + 10:.2f}")
        case "CNX UBP":
            print(f"{(weight * 40) + 15:.2f}")
        case "UBP BKK":
            print(f"{(weight * 40) + 20:.2f}")
        case "BKK PKT":
            print(f"{(weight * 50) + 25:.2f}")
        case "PKT CNX":
            print(f"{(weight * 60) + 30:.2f}")
        case "UBP PKT":
            print(f"{(weight * 70) + 40:.2f}")
        case _:
            print("Error")

main()
