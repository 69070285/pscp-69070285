"""Destiny"""

def main():
    """Main Function"""
    result = ""
    name1 = input().upper()
    name2 = input().upper()
    if len(name1) < len(name2):
        name1 = (name1 * len(name2))[:len(name2)]
    else:
        name2 = (name2 * len(name1))[:len(name1)]

    for n1, n2 in zip(name1, name2):
        if n1 in "LOVE" or n2 in "LOVE":
            result += "w"
        else:
            result += "$"

    max_w = len(max(result.split("$")))
    if result.count("w") % 2:
        print(result + str(max_w))
    elif max_w >= 2:
        print(result)
    else:
        print(result + "#")

main()
