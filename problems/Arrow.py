"""Arrow"""

def main():
    """Main Function"""
    command = input()
    center = int(input())
    height = center * 2 - 1

    for count, direction in enumerate(command):
        match direction:
            case "R":
                for i in range(height):
                    if i < center:
                        print(" " * (i * 2) + "*" * (center - i),)
                    else:
                        print(" " * ((height - i - 1) * 2) + "*" * (i + 2 - center))
            case _:
                for i in range(height):
                    if i < center:
                        print(" " * (center - i - 1) + "*" * (center - i),)
                    else:
                        print(" " * (abs(i + 1 - center)) + "*" * (i + 2 - center))

        if not count == len(command) - 1:
            print()

main()
