"""Classify"""

def main():
    """Main Function"""
    data = sorted(list(iter(input, "END")))
    cutout = [d[:4] for d in data]
    year = []
    branch = []

    for s_id in data:
        if s_id[:4] in branch:
            continue
        if s_id[:2] not in year:
            print(s_id[:2], int(s_id[2:4]), cutout.count(s_id[:4]))
            year.append(s_id[:2])
        else:
            print("--", int(s_id[2:4]), cutout.count(s_id[:4]))

        branch.append(s_id[:4])

main()
