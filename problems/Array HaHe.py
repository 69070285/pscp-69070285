"""Array HaHe"""

def main():
    """Main Function"""
    numbers = []
    for i in range(1, 4):
        numbers.append(int(input()))
        print(f"Input number {i} stored.")
    ori = numbers
    des = sorted(numbers, reverse=True)
    asc = sorted(numbers)

    while True:
        command = int(input())
        match command:
            case 1:
                print("Original order:", *ori)
            case 2:
                print("Descending order:", *des)
            case 3:
                print("Ascending order:", *asc)
            case _:
                return

main()
