"""Conan"""

def main():
    """Main Function"""
    text = input()
    num = int(input()) % 26
    result = []

    for i in text:
        result.append(chr((ord(i) - 97 + num) % 26 + 97))

    print("".join(result))

main()
