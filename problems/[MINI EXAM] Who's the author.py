"""[MINI EXAM] Who's the author"""

def main():
    """Main Function"""
    storage = {}

    while True:
        data = input().split()
        if data[0] == "END":
            break
        if data[0] not in storage:
            storage[data[0]] = []
        if data[1] not in storage[data[0]]:
            storage[data[0]].append(data[1])

    if storage:
        for k, v in storage.items():
            print(f"{k}: {v}")
    else:
        print("No Information")

main()
