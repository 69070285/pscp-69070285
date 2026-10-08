"""[LEARNING LOGS] Impostor"""

from json import loads

def main():
    """Main Function"""
    alive = {}
    dead = {}

    while True:
        data = input()
        if data == "Start":
            break
        alive.update(loads(data))

    while True:
        kill = input()
        if kill == "End":
            break
        dead[kill] = alive[kill]
        del alive[kill]

    print(f"{list(alive.values()).count("Impostor")} Impostor Remains")
    print("***Alive***")
    for key, value in sorted(alive.items()):
        print(f"{key} : {value}")
    print("***Dead***")
    for key, value in sorted(dead.items()):
        print(f"{key} : {value}")

main()
