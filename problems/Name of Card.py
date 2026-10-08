"""Name of Card"""

def main():
    """Main Function"""
    front_card = {"A": "Ace", "J": "Jack", "Q": "Queen", "K": "King"}
    back_card = {"D": "Diamonds", "H": "Hearts", "S": "Spades", "C": "Clubs"}
    data = input().upper()

    if data[0] == "1":
        print(f"10 of {back_card[data[-1]]}")
    elif data[0].isalpha():
        print(f"{front_card[data[0]]} of {back_card[data[-1]]}")
    else:
        print(f"{data[0]} of {back_card[data[-1]]}")

main()
