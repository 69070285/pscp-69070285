"""[MINI EXAM] Hamming"""

def main():
    """Main Function"""
    text1 = input()
    text2 = input()
    count = sum(1 for t1, t2 in zip(text1, text2) if t1 != t2)
    print(count)

main()
