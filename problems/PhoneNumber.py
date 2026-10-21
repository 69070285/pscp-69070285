"""PhoneNumber"""

def main():
    """Main Function"""
    n = input()
    place = input()

    if place == "Domestic":
        print(f"{n[0]} {n[1:5]} {n[5:]}" if len(n) < 10 else f"{n[:2]} {n[2:6]} {n[6:]}")
    else:
        print(f"+66 {n[1:5]} {n[5:]}" if len(n) < 10 else f"+66{n[1]} {n[2:6]} {n[6:]}")

main()
