"""[MINI EXAM] Longer"""

from math import pi

def main():
    """Main Function"""
    r = float(input())
    a = float(input())
    b = float(input())
    circle = 2 * pi * r
    rectangle = (a * 2) + (b * 2)

    if circle > rectangle:
        print("Circle is longer")
        print(f"{circle - rectangle:.5f}")
    elif circle < rectangle:
        print("Rectangle is longer")
        print(f"{rectangle - circle:.5f}")
    else:
        print("Equal")
        print(f"{0:.5f}")

main()
