"""Game"""

def main():
    """Main Function"""
    a, b = int(input()) % 3, int(input()) % 3
    print(a if a == b else "Error")

main()
