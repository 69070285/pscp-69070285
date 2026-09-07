"""Put In A Box"""

def main():
    """Main Function"""
    width, lenght, r_start, r_end = map(int, input().split())
    result = []

    for i in range(r_start, r_end + 1):
        result.append((width % i) * (lenght % i))

    print(min(result))

main()
