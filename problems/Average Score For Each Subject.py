"""Average Score For Each Subject"""

def main():
    """Main Function"""
    amount = int(input())
    total = []
    is_pass = True

    for _ in range(amount):
        score = int(input())
        if score < 50:
            is_pass = False
        total.append(score)

    average = sum(total) / amount
    print(f"{average:.1f}")
    if is_pass and average >= 60:
        print("PASS")
    else:
        print("FAIL")

main()
