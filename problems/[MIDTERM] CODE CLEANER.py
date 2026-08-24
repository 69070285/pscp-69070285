"""[MIDTERM] CODE CLEANER"""

def main():
    """Main Function"""
    text = input()
    result = ""
    last = ""
    letter = 0
    digit = 0

    for i in text:
        if i.isalnum():
            if not last and result:
                result += "-"
            result += i.upper()
            last = i
            if i.isalpha():
                letter += 1
            else:
                digit += 1
        elif not i.isalnum():
            last = ""
    if not result:
        print("CODE = NONE")
    else:
        print(f"CODE = {result}")
    print(f"LETTERS = {letter}")
    print(f"DIGITS = {digit}")

main()
