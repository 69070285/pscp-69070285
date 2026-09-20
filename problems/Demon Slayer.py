"""Demon Slayer"""

def main():
    """Main Function"""
    demon = [
        ["Spider Demon", 1], ["Swamp Demon", 2], ["Arrow Demon", 1], ["Hand Demon", 2],
        ["Drum Demon", 3], ["Mugen Train", 2], ["Upper Moon", 3]
    ]
    kill = 0
    attack = 0

    while demon and kill < 5:
        d = demon.pop(0)
        for i in range(2):
            attack += 1
            command = int(input())
            if command == d[1]:
                print(d[0])
                print("kill")
                kill += 1
                break
            if i == 1:
                print(d[0])
                demon.append(d)
                print("back")

    print(attack)

main()
