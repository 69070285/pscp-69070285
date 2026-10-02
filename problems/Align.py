"""Align"""

def main():
    """Main Function"""
    size = int(input())
    align = input()
    text = input()

    if align == "left":
        print(text.ljust(size))
    elif align == "right":
        print(text.rjust(size))
    else:
        padding = size - len(text)
        if padding > 0:
            left_padding = (padding // 2) + (padding % 2)
            right_padding = padding // 2
            print(" " * left_padding + text + " " * right_padding)
        else:
            print(text)

main()
