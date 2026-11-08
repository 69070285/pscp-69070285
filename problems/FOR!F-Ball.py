"""FOR!F-Ball"""

def main():
    """Main Function"""
    pos, check = "A", "ABC"

    for move in input():
        if move == "A" and pos in "AB":
            pos = "B" if pos == "A" else "A"
        elif move == "B" and pos in "BC":
            pos = "C" if pos == "B" else "B"
        elif move == "C" and pos in "CA":
            pos = "A" if pos == "C" else "C"

    print(check.find(pos) + 1)

main()
