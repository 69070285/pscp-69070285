"""Warehouse Management System"""

def main():
    """Main Function"""
    storage = {}

    while True:
        cmd = input().split()
        if cmd[0] == "END":
            break

        if cmd[0] == "ADD":
            item, qty = cmd[1], int(cmd[2])
            storage[item] = storage.get(item, 0) + qty
        elif cmd[0] == "REMOVE":
            item, qty = cmd[1], int(cmd[2])
            if item not in storage or storage[item] < qty:
                print(f"Not enough stock for {item}")
                storage[item] = 0
            else:
                storage[item] -= qty
        elif cmd[0] == "CHECK":
            low_stock = [key for key, val in sorted(storage.items()) if val < 5]
            if low_stock:
                for item in low_stock:
                    print(item)
            else:
                print("All stocks are sufficient")
        elif cmd[0] == "REPORT":
            for key, value in sorted(storage.items()):
                print(f"{key}: {value}")

main()
