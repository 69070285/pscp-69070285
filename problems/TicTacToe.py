"""TicTacToe"""

def main():
    """Main Function"""
    row1, row2, row3 = input(), input(), input()
    com1, com2 = row1[2] + row2[1] + row3[0], row1[0] + row2[1] + row3[2]
    com3, com4 = row1[0] + row2[0] + row3[0], row1[1] + row2[1] + row3[1]
    com5 = row1[2] + row2[2] + row3[2]

    if "XXX" in (row1, row2, row3, com1, com2, com3, com4, com5):
        print("X WIN")
    elif "OOO" in (row1, row2, row3, com1, com2, com3, com4, com5):
        print("O WIN")
    else:
        print("DRAW")

main()
