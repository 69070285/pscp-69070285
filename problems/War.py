"""War"""

import json

def main():
    """Main Function"""
    allies = sorted(json.loads(input()), reverse=True)
    enemies = sorted(json.loads(input()), reverse=True)
    survive, i = 0, 0

    for a in allies:
        while i < len(enemies) and enemies[i] >= a:
            i += 1
        if i == len(enemies):
            break
        survive += a
        i += 1

    print(survive)

main()
