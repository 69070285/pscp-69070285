"""[MIDTERM] ijudge-itkmitl"""

def main():
    """Main Function"""
    text = input()
    if not text[39:43].isnumeric():
        text = ""

    if ("https://ijudge.it.kmitl.ac.th/problems/" in text) and (len(text) >= 43) and \
        (int(text[39:43]) >= 0) and len(text[39:43]) == 4 and 0 <= int(text[39]) <= 3:
        print(f"{text[39]} STAR")
    else:
        print("INVALID")

main()
