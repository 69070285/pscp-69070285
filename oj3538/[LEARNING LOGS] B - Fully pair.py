"""[LEARNING LOGS] B - Fully pair?"""

def main():
    """Main Function"""
    text = input()
    sad = ""

    for char in text:
        if text.count(char) % 2 and char not in sad:
            sad += char

    print(sad if sad else "fully paired")

main()
