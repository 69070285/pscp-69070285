"""Electric_Using"""

def main():
    """Main Function"""
    unit = float(input())
    ft = unit * 0.5

    if unit > 200:
        total = 2030 + ((unit - 200) * 15)
    elif unit > 100:
        total = 830 + ((unit - 100) * 12)
    elif unit > 50:
        total = 330 + ((unit - 50) * 10)
    elif unit > 10:
        total = 50 + ((unit - 10) * 7)
    else:
        total = unit * 5

    print(f"{(total * 1.07) + ft:.1f}")

main()
