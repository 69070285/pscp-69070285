"""BookWorm"""

def main():
    """Main Function"""
    for _ in range(int(input())):
        time, read = float(input()), 0
        book = sorted([float(input()) for _ in range(int(input()))])
        for b in book:
            if time >= b:
                read += 1
                time -= b
        print(read)

main()
