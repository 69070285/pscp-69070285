"""THEOS Text"""

def main():
    """Main Function"""
    text, seen = input(), []
    for c in text:
        if c not in seen:
            seen.append(c)
    print("".join(str(text.count(c)) + c for c in seen))

main()
