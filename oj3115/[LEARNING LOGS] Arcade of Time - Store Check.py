"""[LEARNING LOGS] Arcade of Time: Store Check"""

def main():
    """Main Function"""
    amount, check = map(int, input().split())
    store = []
    result = []
    count = 0
    for _ in range(amount):
        time = input().split()
        store.append(time)
    check_time = input().split()

    for i in range(check):
        for _, time_range in enumerate(store):
            if int(time_range[0]) <= int(check_time[i]) < int(time_range[1]):
                count += 1
        result.append(str(count))
        count = 0

    print(" ".join(result))

main()
