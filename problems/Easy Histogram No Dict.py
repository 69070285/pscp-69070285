"""Easy Histogram No Dict"""

def main():
    """Main Function"""
    used = []
    text = input()
    text = sorted([i for i in text if i.isalpha()], key=lambda l: ord(l.lower()))

    for i in text:
        if i.upper() not in used:
            used.append(i.upper())
            if i.lower() in text:
                print(f"{i.lower()} = {text.count(i.lower())}")
            if i.upper() in text:
                print(f"{i.upper()} = {text.count(i.upper())}")

main()
