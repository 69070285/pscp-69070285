"""No 13th Floor"""

def main():
    """Main Function"""
    code = input()
    digits = [int(i) for i in code]
    add = sum(digits)
    mul = 1
    for i in digits:
        mul *= i
    result = ""

    for i in range(5):
        if digits[i] > 5 and i == 4:
            result += "14"
            break
        if digits[i] > 5:
            result += str(9 + i)
            break
    if not result:
        result += "13"

    if (code == code[::-1] and digits[0] + digits[4] > 5) or\
        (digits[4] and digits[0] // digits[4] > 5):
        result += "1"
    elif (code == code[::-1] and digits[1] * digits[3] > 5) or\
        (digits[1] - digits[4] > 5):
        result += "2"
    else:
        result += "0"

    if add > 25:
        result += "1"
    elif mul > 55:
        result += "2"
    else:
        result += "0"

    print(result)

main()
