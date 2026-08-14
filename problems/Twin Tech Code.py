"""Twin Tech Code"""

def main():
    """Main Function"""
    digit = int(input())
    first = input()
    second = input()
    result = 0

    for i in range(digit):
        if int(first[i]) + int(second[i]) != 9:
            result += 1

    if not result:
        print("YES")
    else:
        print("NO", result)

main()
