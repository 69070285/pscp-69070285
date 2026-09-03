"""[LEARNING LOGS] Flower Bed"""

from math import ceil

def main():
    """Main Function"""
    thick, target = map(int, input().split())
    result = 0
    floor = 0

    while result < target:
        floor += 1
        result += floor

    print(ceil(floor / thick))

main()
