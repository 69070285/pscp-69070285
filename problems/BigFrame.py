"""BigFrame"""

def main():
    """Main Function"""
    all_word = []
    long = 0
    for i in range(5):
        word = " " + input().strip() + " "
        if len(word) > long:
            long = len(word)
        all_word.append(word)

    print("*" * (long + 2))
    for i in all_word:
        print("*" + i + " " * (long - len(i)) + "*")
    print("*" * (long + 2))

main()
