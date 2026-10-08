"""FourDirections"""

def main():
    """Main Function"""
    directions = {
        "U": [
            "  *   ",
            " ***  ",
            "* * * ",
            "  *   ",
            "  *   "
        ],
        "D": [
            "  *   ",
            "  *   ",
            "* * * ",
            " ***  ",
            "  *   "
        ],
        "L": [
            "  *   ",
            " *    ",
            "***** ",
            " *    ",
            "  *   "
        ],
        "R": [
            "  *   ",
            "   *  ",
            "***** ",
            "   *  ",
            "  *   "
        ]
    }

    command = input()
    command = [directions[d] for d in command]

    for row in range(5):
        print("".join(c[row] for c in command))

main()
