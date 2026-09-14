"""BusStop I"""

def main():
    """Main Function"""
    seat = int(input())
    station = int(input())
    stop = [list(map(int, input().split())) for _ in range(station)]
    stop.sort(key=lambda r: r[0])
    passenger = []
    success = 0

    for bus_stop in stop:
        current = bus_stop[0]
        queue = bus_stop[1:]

        while current in passenger:
            passenger.remove(current)
            success += 1

        for destination in queue:
            if destination > current and len(passenger) < seat:
                passenger.append(destination)

    print(success)

main()
