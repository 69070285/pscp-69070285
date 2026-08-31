"""Little Bunny Loves BUU"""

def main():
    """Main Function"""
    text = input()
    b_pos = text.lower().find("b")
    is_b = False
    u_count = 0
    max_u = 0

    for letter in text.lower():
        if letter == "b":
            is_b = True
            u_count = 0
        elif letter == "u" and is_b:
            u_count += 1
        else:
            is_b = False

        if u_count > max_u and u_count >= 2:
            max_u = u_count

    if max_u:
        print(f"Yes {max_u}")
    elif "b" in text.lower():
        print(text[:b_pos + 1] + "U" * (len(text) - (b_pos + 1)))
    else:
        print(("BUU" * len(text))[:len(text)])

main()
