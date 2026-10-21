"""Key_Midterm2014"""

def main():
    """Main Function"""
    number = input()
    rule1 = sum(int(n) for n in number)
    rule2 = int(number[-3:]) * 10
    rule3 = rule1 + rule2
    print(str(rule3)[-4:] if len(str(rule3)) >= 4 else str(rule3 + 1000)[-4:])

main()
