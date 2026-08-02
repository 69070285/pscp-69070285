"""Promotion Product Price"""

def main():
    """Main Function"""

    pencil, book, color = map(int, input().split())

    if pencil + book + color >= 3:
        print(int((pencil * 25 + book * 40 + color * 55) * 0.9))
    else:
        print(pencil * 25 + book * 40 + color * 55)

main()
