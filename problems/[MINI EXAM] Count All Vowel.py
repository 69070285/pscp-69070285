"""[MINI EXAM] Count All Vowel"""

def main():
    """Main Function"""
    amount = int(input())
    count = 0
    a = False
    e = False
    i = False
    o = False
    u = False

    for i in range(amount):
        letter = input()
        if letter in "AEIOU":
            count += 1
            match letter:
                case "A":
                    a = True
                case "E":
                    e = True
                case "I":
                    i = True
                case "O":
                    o = True
                case _:
                    u = True

    print(count)
    if a and e and i and o and u:
        print("YES")
    else:
        print("NO")

main()
