"""[LEARNING LOGS] 44 Cards"""

def main():
    """Main Function"""
    front_card = {"A": "ace", "J": "jack", "Q": "queen", "K": "king"}
    back_card = {"D": "diamonds", "H": "hearts", "S": "spades", "C": "clubs"}
    data = input().upper()

    if data[0] == "1":
        print(f"10 of {back_card[data[-1]]}")
    elif data[0].isalpha():
        print(f"{front_card[data[0]]} of {back_card[data[-1]]}")
    else:
        print(f"{data[0]} of {back_card[data[-1]]}")

main()
