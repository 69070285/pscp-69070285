"""[MINI EXAM] GG-EZ"""

def main():
    """Main Function"""
    game = input()
    score = int(input())

    if (game == "Rov" and score >= 2) or (game == "Valorant" and score >= 7):
        print("GGEZ")
    else:
        print("GGWP")

main()
