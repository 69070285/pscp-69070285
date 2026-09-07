"""The Chaotic Movie Ticket"""

def main():
    """Main Function"""
    seat = int(input())

    while seat > 0:
        try:
            age, amount = map(int, input().split())
        except EOFError:
            break
        if age < 15:
            print("-1")
        elif amount > seat:
            print("-2")
        else:
            seat -= amount
            if 15 <= age <= 22:
                print(f"{int(amount * 150 * 0.8)} {seat}")
            elif age >= 60:
                print(f"{int(amount * 150 * 0.5)} {seat}")
            else:
                print(f"{amount * 150} {seat}")

main()
