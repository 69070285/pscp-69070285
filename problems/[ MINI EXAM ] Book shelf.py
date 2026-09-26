"""[ MINI EXAM ] Book shelf"""

def main():
    """Main Fuction"""
    bookshelf = input().split()
    target = input()

    if target not in bookshelf:
        print("There are no book with that name on this shelf")
    else:
        bookshelf.remove(target)
        print(*bookshelf)

main()
