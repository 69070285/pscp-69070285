"""[LEARNING LOGS] Shorten"""

def main():
    """Main Function"""
    all_num = []
    while True:
        number = int(input())
        if number == -1:
            break
        all_num.append(number)

    result = []
    start = 0
    while start < len(all_num):
        stop = start
        while stop + 1 < len(all_num) and all_num[stop + 1] == all_num[stop] + 1:
            stop += 1
        result.append(f"{all_num[start]}-{all_num[stop]}" if stop > start else str(all_num[start]))
        start = stop + 1

    print(", ".join(result))

main()
