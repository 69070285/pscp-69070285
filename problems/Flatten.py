"""Flatten"""

def main():
    """Main Function"""
    data = list(map(int, input().replace("[", "").replace("]", "").replace(" ", "").split(",")))
    print(sorted(data, reverse=True))

main()
