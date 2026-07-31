"""Suvarnabhumi Airport Parking"""

from math import ceil

start = input().split(".")
stop = input().split(".")
start_second = int(start[0]) * 3600 + int(start[1]) * 60
stop_second = int(stop[0]) * 3600 + int(stop[1]) * 60
start_check = 0 <= int(start[0]) <= 24 and 0 <= int(start[1]) <= 60
stop_check = 0 <= int(stop[0]) <= 24 and 0 <= int(stop[1]) <= 60
hour = (stop_second - start_second) / 3600

if hour > 0.25:
    hour = ceil(hour)
elif hour < 0:
    hour = -1
else:
    hour = 0

if 0 <= hour <= 24 and start_check and stop_check:
    match hour:
        case 0:
            print("FREE")
        case 1:
            print("25")
        case 2:
            print("50")
        case 3:
            print("80")
        case 4:
            print("110")
        case 5:
            print("145")
        case 6:
            print("180")
        case _:
            print("250")
else:
    print("ERROR")
