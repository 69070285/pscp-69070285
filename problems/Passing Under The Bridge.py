"""Passing Under The Bridge"""

def main():
    """Main Function"""
    max_pass = 0
    distance, amount = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(amount)]

    for i in range(1, distance + 1):
        count = 0
        for b in bridges:
            if b[0] < i <= b[1]:
                count += 1
        if count > max_pass:
            max_pass = count

    print(max_pass)

main()
