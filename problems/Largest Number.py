"""Largest Number"""

def main():
    """Main Function"""
    n1, n2, n3 = input(), input(), input()

    if int(n1 + n2) < int(n2 + n1):
        n1, n2 = n2, n1
    if int(n1 + n3) < int(n3 + n1):
        n1, n3 = n3, n1
    if int(n2 + n3) < int(n3 + n2):
        n2, n3 = n3, n2

    print(int(n1 + n2 + n3))

main()
