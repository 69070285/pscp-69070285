"""[MIDTERM] Triangle"""

def main():
    """Main Function"""
    a = int(input())
    b = int(input())
    c = int(input())

    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("EQUILATERAL")
        elif c**2 == a**2 + b**2 or a**2 == b**2 + c**2 or b**2 == a**2 + c**2:
            print("RIGHT TRIANGLE")
        elif a == b or a == c or b == c:
            print("ISOSCELES")
        else:
            print("SCALENE")
    else:
        print("NOT A TRIANGLE")

main()
