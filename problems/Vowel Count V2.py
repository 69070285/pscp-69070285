"""Vowel Count V2"""

def main():
    """Main Function"""
    text = input()
    result = 0
    for i in text:
        if i in ("a", "e", "i", "o", "u"):
            result += 1

    print(result)

main()
