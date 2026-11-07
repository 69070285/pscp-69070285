"""Count The Vowels and Find The Longest Consecutive Vowels"""

def main():
    """Main Function"""
    for n in range(1, int(input()) + 1):
        vowel, con, mx_con = 0, 0, 0
        for ch in input().lower():
            if ch in "aeiou":
                vowel, con = vowel + 1, con + 1
            else:
                con = 0
            if con > mx_con:
                mx_con = con
        print(f"Line {n}: vowels = {vowel}, max_consecutive = {mx_con}")

main()
