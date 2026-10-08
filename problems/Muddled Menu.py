"""Muddled Menu"""

def main():
    """Main Function"""
    course = []

    while True:
        order = input()

        if order == "CLOSED":
            course.clear()
            break
        if order == "DONE":
            break
        if order == "SOMETHING'S WRONG":
            course.clear()
        elif "Can't do: " in order:
            course.remove(order.split(": ")[1])
        elif "#N" in order:
            course.append(order.split(" #")[0])
        else:
            course.insert(int(order.split(" #")[1]) - 1, order.split(" #")[0])

    print(f"Full Course: {course} Reversed: {course[::-1]}")

main()
