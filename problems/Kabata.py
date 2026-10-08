"""Kabata"""

def main():
    """Main Function"""
    amount = int(input())

    for _ in range(amount):
        word = input().replace("bakka", " ").replace("baka", "-")
        word = word.replace("ka", "").replace("ba", "").replace("ta", "").replace(" ", "")

        if not word:
            print("yes")
        else:
            print("no")

main()
