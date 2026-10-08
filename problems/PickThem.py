"""PickThem"""

import json

def main():
    """Main Function"""
    data = json.loads(input())
    even = [i for i in data if not i % 2]

    if not even:
        print("Nope")
    else:
        for i in even:
            print(i)

main()
