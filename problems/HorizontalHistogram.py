"""HorizontalHistogram"""

def main():
    """Main Function"""
    used = []
    text = sorted(list(input()), key=lambda c: (c.isupper(), ord(c)))

    for c in text:
        if c in used:
            continue
        amount = text.count(c)
        group = amount // 5
        remain = amount % 5
        collect = ["-----"] * group
        if remain > 0:
            collect.append("-" * remain)
        used.append(c)

        print(f"{c} : {"|".join(collect)}")

main()
