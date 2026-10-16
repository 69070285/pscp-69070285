"""Hint"""

def main():
    """Main Function"""
    digits = []
    for _ in range(3):
        sign, num = input().split()
        num = int(num)
        match sign:
            case "==":
                collect = [i for i in range(10) if i == num]
            case "!=":
                collect = [i for i in range(10) if i != num]
            case "<":
                collect = [i for i in range(10) if i < num]
            case ">":
                collect = [i for i in range(10) if i > num]
            case "<=":
                collect = [i for i in range(10) if i <= num]
            case _:
                collect = [i for i in range(10) if i >= num]
        digits.append(collect)

    for i in digits[2]:
        for j in digits[1]:
            for k in digits[0]:
                print(f"{i}{j}{k}")

main()
