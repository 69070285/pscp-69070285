"""PairNumbering"""

import json

def main():
    """Main Function"""
    a_list, b_list, target = json.loads(input()), json.loads(input()), int(input())
    b_dict, count = {}, 0

    for b in b_list:
        b_dict[b] = b_dict.get(b, 0) + 1

    for a in a_list:
        count += b_dict.get(target - a, 0)

    print(count)

main()
