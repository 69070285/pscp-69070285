"""Resistor"""

def main():
    """Main Function"""
    band = {
        "Black": "0", "Brown": "1", "Red": "2", "Orange": "3", "Yellow": "4",
        "Green": "5", "Blue": "6", "Purple": "7", "Grey": "8", "White": "9"
    }
    multiplier = {
        "Black": 1, "Brown": 10, "Red": 100, "Orange": 1000, "Yellow": 10000,
        "Green": 100000, "Blue": 1000000, "Purple": 10000000, "Gold": 0.1, "Silver": 0.01
    }
    tolerance = {
        "Brown": 1, "Red": 2, "Green": 0.5, "Blue": 0.25, "Purple": 0.1,
        "Grey": 0.05, "Gold": 5, "Silver": 10
    }

    b1 = input()
    b2 = input()
    mul = input()
    tol = input()

    if b1 in band and b2 in band and mul in multiplier and tol in tolerance:
        print(f"{int(band[b1] + band[b2]) * multiplier[mul] * (1 - tolerance[tol] / 100):.4f}")
        print(f"{int(band[b1] + band[b2]) * multiplier[mul] * (1 + tolerance[tol] / 100):.4f}")
    else:
        print("Error")

main()
