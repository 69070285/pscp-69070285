"""iPhone 13 Again"""

def main():
    """Main Function"""
    iphone = {
        "iPhone 13 mini": 25900, "iPhone 13": 29900,
        "iPhone 13 Pro": 38900, "iPhone 13 Pro Max": 42900
    }
    storage = {"128 GB": 0, "256 GB": 4000, "512 GB": 12000, "1 TB": 20000}
    base = input()
    extra = input()

    if base not in iphone or extra not in storage or\
    (base in ("iPhone 13 mini", "iPhone 13") and extra == "1 TB"):
        print("Not Available")
    else:
        print(iphone[base] + storage[extra])

main()
