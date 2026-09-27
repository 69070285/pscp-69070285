"""Filter"""

from json import loads

def main():
    """Main Function"""
    data = loads(input())
    target = float(input())
    result = sorted([[key, f"{value:.2f}"] for key, value in data.items() if value >= target])

    if not result:
        print("Nope")
    else:
        for r in result:
            print(*r, sep="\t")

main()
