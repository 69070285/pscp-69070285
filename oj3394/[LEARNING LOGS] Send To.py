"""[LEARNING LOGS] Send To"""

def main():
    """Main Function"""
    amount, send = map(int, input().split())
    data = [0] + [int(input()) for _ in range(amount)]
    used = [0]
    count = 0

    while send not in used:
        used.append(send)
        send = data[send]
        count += 1

    print(count)

main()
