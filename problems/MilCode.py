"""MilCode"""

def main():
    """Main Function"""
    result, check = "", "*+/#"

    for num in input().split():
        if not int(num):
            result += "-"
        else:
            add = ""
            for i, n in enumerate(num[::-1]):
                add += check[i] if int(n) else ""
            result += add[::-1]

    print(result)

main()
