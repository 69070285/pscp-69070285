"""CaesarV2"""

def main():
    """Main Function"""
    text = input()
    common_words = ("what", "when", "why", "which", "this", "there", "where", "the", "is", "am"\
    ,"are", "you", "we", "they", "he", "she", "it")

    for s in range(26):
        decrypted = ""
        for c in text:
            if c.isupper():
                decrypted += chr((ord(c) + s - 65) % 26 + 65)
            elif c.islower():
                decrypted += chr((ord(c) + s - 97) % 26 + 97)
            else:
                decrypted += c

        decrypted = decrypted.split()
        if any(w.strip(".") in common_words for w in decrypted):
            print(*decrypted)
            return

main()
