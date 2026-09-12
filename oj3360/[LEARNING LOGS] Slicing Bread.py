"""[LEARNING LOGS] Slicing Bread"""

def main():
    """Main Function"""
    width, lenght, col, row = map(int, input().split())
    col_knife = ("0 " + input() + " " + str(width))
    col_knife = list(map(int, col_knife.split()))
    row_knife = "0 " + input() + " " + str(lenght)
    row_knife = list(map(int, row_knife.split()))
    bread = []

    for i in range(1, col + 2):
        for j in range(1, row + 2):
            bread.append((col_knife[i] - col_knife[i - 1]) * (row_knife[j] - row_knife[j - 1]))

    bread.sort(reverse=True)
    print(*bread[:2])

main()
