"""Rabbit Language"""

def main():
    """Main Function"""
    text = input().upper()
    n = len(text)
    if all(letter in "IT" for letter in text):
        return print(f"unknown {n}")

    i, max_a = 0, 0
    while i < n:
        if text[i] == "R":
            if i + 1 >= n:
                return print(f"no {i}")
            if text[i + 1] != "A":
                return print(f"no {i + 1}")
            start = i + 1
            i += 1
            while i < n and text[i] == "A":
                i += 1
            max_a = max(max_a, i - start)
        elif text[i] == "B":
            if i + 1 >= n:
                return print(f"no {i}")
            if text[i + 1] not in "IT":
                return print(f"no {i + 1}")
            i += 1
            while i < n and text[i] in "IT":
                i += 1
        elif text[i] in "IT":
            i += 1
        else:
            return print(f"no {i}")

    return print(f"yes {max_a}")

main()
