"""PongYa"""

def main():
    """Main Function"""
    num = input()
    print("PONG" if not int(num) % 3 or num[-1] == "3" else num)

main()
