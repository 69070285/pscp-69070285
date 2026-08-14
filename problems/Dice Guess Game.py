"""Dice Guess Game"""

def main():
    """Main Function"""
    guess = int(input())
    correct = int(input())
    check_guess = 1 <= guess <= 6
    check_correct = 1 <= correct <= 6

    if guess == correct and check_guess and check_correct:
        print("Correct!")
    elif guess != correct and check_guess and check_correct:
        print("Wrong!")
    else:
        print("Invalid")

main()
