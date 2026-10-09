"""Turnstile"""

def main():
    """Main Function"""
    count, last = 0, ""

    while True:
        action = input()
        if action == "END":
            return print(count)
        if action == "P" and last == "C":
            count += 1
        last = action

main()
