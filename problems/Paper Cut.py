"""Paper Cut"""

def main():
    """Main Function"""
    width, lenght = map(int, input().split())
    col, row = map(int, input().split())
    col_cut = ("0 " + input() + " " + str(width))
    col_cut = list(map(int, col_cut.split()))
    row_cut = "0 " + input() + " " + str(lenght)
    row_cut = list(map(int, row_cut.split()))
    paper = []

    for i in range(1, col + 2):
        for j in range(1, row + 2):
            paper.append((col_cut[i] - col_cut[i - 1]) * (row_cut[j] - row_cut[j - 1]))

    paper.sort(reverse=True)
    print(*paper[:2], sep="\n")

main()
