"""Teaching Schedule"""

def main():
    """Main Function"""
    classPerWeek = int(input())
    minutePerClass = int(input())
    total = classPerWeek * minutePerClass
    hour = total // 60
    minute = total % 60

    if not total:
        print("No teaching")
    elif hour and minute:
        print(f"{hour} hours {minute} minute")
    elif not minute:
        print(f"{hour} hours")
    else:
        print(f"{minute} minute")

main()
